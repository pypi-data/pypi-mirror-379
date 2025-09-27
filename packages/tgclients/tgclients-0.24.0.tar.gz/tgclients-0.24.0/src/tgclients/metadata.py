# SPDX-FileCopyrightText: 2022 Georg-August-Universität Göttingen
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Helper functions to work with TextGrid metadata XML."""

import logging
import os
import re
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from tgclients.databinding.textgrid_metadata_2010 import MetadataContainerType
from tgclients.databinding.tgsearch import Response, ResultType

try:
    import icu
except ImportError:
    icu = None

logger = logging.getLogger(__name__)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TextgridMetadata:
    """Helper functions to work with TextGrid metadata XML."""

    def __init__(self):
        context = XmlContext()
        self._parser = XmlParser(context=context)
        self._file_extension_map = self._build_extension_map()
        if icu is not None:
            self._transliterator = self._create_transliterator()
        else:
            logger.warning('Transliterating without PyICU, you may need that for correct results')

    @staticmethod
    def create(title: str, mimetype: str) -> str:
        """Create XML metadata for an TextGrid Object.

        Args:
            title (str): title of the object
            mimetype (str): format / MIME type of the object

        Returns:
            str: XML metadata as string
        """
        path = Path(__file__).parent / 'templates'
        env = Environment(loader=FileSystemLoader(Path(path)), autoescape=True)
        template = env.get_template('metadata.xml.jinja2')
        metadata = template.render(title=title, format=mimetype)
        return metadata

    def build(self, title: str, mimetype: str) -> MetadataContainerType:
        """Build metadata for an TextGrid Object.

        Args:
            title (str): title of the object
            mimetype (str): format / MIME type of the object

        Returns:
            MetadataContainerType: metadata
        """
        metadata = TextgridMetadata().create(title, mimetype)
        return self._parser.from_string(metadata, MetadataContainerType)

    def searchresponse2object(self, xml: str) -> Response:
        """Build databinding for XML string returned from tgsearch.

        Args:
            xml (str): xml string as returned from tgsearch

        Returns:
            Response: tgsearch Response
        """
        return self._parser.from_string(xml, Response)

    def filename_from_metadata(self, metadata: ResultType) -> str:
        """Generate a filename for a textgrid search metadata result.

        This is made of title, textgrid-URI and extension.

        Args:
            metadata (ResultType): tgsearch metadata result

        Returns:
            str: the filename
        """
        if metadata.authorized is False:
            title = 'Restricted TextGrid Object'
            mimetype = None
        else:
            title = metadata.object_value.generic.provided.title[0]
            mimetype = metadata.object_value.generic.provided.format
        uri = metadata.object_value.generic.generated.textgrid_uri.value
        return self.filename(title, uri, mimetype)

    def filename(self, title: str, tguri: str, mimetype: str) -> str:
        """Generate a filename for the triple of title, textfgrid-uri and extension.

        Args:
            title (str): the title
            tguri (str): the textgrid uri
            mimetype (str): the mime type (e.g. 'text/xml')

        Returns:
            str: the filename
        """
        title = self.transliterate(title)
        tg_id = self.remove_tg_prefix(tguri)
        ext = self.extension_for_format(mimetype)
        if ext is not None:
            return f'{title}.{tg_id}.{ext}'
        else:
            return f'{title}.{tg_id}'

    def _build_extension_map(self) -> dict:
        # converted to python from info.textgrid.utils.export.filenames.FileExtensionMap
        # of link-rewriter (https://gitlab.gwdg.de/dariah-de/textgridrep/link-rewriter)
        extension_map = {}
        map_line_pattern = re.compile('^[ \t]*([^# \t]+)[ \t]*([^#]+)[ \t]*(#.*)?$')
        space_pattern = re.compile('[ \t]+')

        with open(os.path.join(__location__, 'mime.types'), encoding='utf8') as mimefile:
            for line in mimefile.readlines():
                line_match = map_line_pattern.match(line.rstrip('\n'))
                if line_match is not None:
                    entry = space_pattern.split(line_match.group(2))
                    # extend the list in the dict, so extensions definded first are first in list
                    if line_match.group(1) not in extension_map:
                        extension_map[line_match.group(1)] = entry
                    else:
                        extension_map[line_match.group(1)].extend(entry)

        return extension_map

    def extension_for_format(self, mimetype: str) -> Optional[str]:
        """Find a matching extension for a textgrid mime type.

        The first matching extension for a mime type is returned, so
        extensions defined first in mime.types will be used.

        Args:
            mimetype (str): the mime type, as found in textgrid
                            metadata format field (e.g. text/xml)

        Returns:
            Optional[str]: a filename extension
        """
        if mimetype in self._file_extension_map:
            return self._file_extension_map[mimetype][0]
        else:
            return None

    @staticmethod
    def remove_tg_prefix(tguri: str) -> str:
        """Remove the 'textgrid:' prefix from an textgrid URI.

        Args:
            tguri (str): the textgrid URI

        Returns:
            str: uri without the prefix
        """
        return tguri[9:]

    @staticmethod
    def id_from_filename(filename: str) -> str:
        """Extract the id from a filename.

        This is named according to link rewriters
        textgrid metadata to filename mapping.

        Args:
            filename (str): the filename

        Returns:
            str: the id
        """
        last_dot = filename.rfind('.')
        next_to_last_dot = filename.rfind('.', 0, last_dot)
        # a textgrid uri has a revision number in the end.
        # if the chars after the last dot are not numeric, we have a filename extension
        if not filename[last_dot + 1 :].isnumeric():
            # extension is there? we need the '.' before the dot separating the uri
            # from the revision component
            next_to_last_dot = filename.rfind('.', 0, next_to_last_dot)
        else:
            # there is no extension to cut of, we want the end of the string
            last_dot = None

        return filename[next_to_last_dot + 1 : last_dot]

    def transliterate(self, title: str) -> str:
        """Replace all chars which may be problematic in filenames from title string.

        Args:
            title (str): a title from textgrid metadata

        Returns:
            str: the title string with problematic chars replaced
        """
        name: str = ''
        if icu is None:
            name = title.replace(' ', '_').replace(']', '_').replace('[', '_').replace(':', '_')
        else:
            name = self._transliterator.transliterate(title)
        return name

    # return type needs to be hidden, because it is not available if PyICU is not installed
    def _create_transliterator(self):
        with open(os.path.join(__location__, 'tgfilenames.rules'), encoding='utf8') as rulesfile:
            rules = rulesfile.read()
            return icu.Transliterator.createFromRules(
                'TgFilenames', rules, icu.UTransDirection.FORWARD
            )
