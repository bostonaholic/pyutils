'''
Created on Sep 8, 2009

@author: mboston
@attention: This is a Jython script and must be compiled and run with Jython
'''

import sys
try:
    import java.io.File;
    import javax.xml.parsers.DocumentBuilder;
    import javax.xml.parsers.DocumentBuilderFactory;
    import javax.xml.transform.dom.DOMSource;
    import javax.xml.validation.Schema;
    import javax.xml.validation.SchemaFactory;
    import javax.xml.validation.Validator;
    import javax.xml.XMLConstants;
    import org.w3c.dom.Document;
except ImportError:
    print("Unable to import the Java libraries.  Be sure you have Jython installed.")
    sys.exit(2)

class XmlValidator(object):
    xml = None
    xsd = None

    def __init__(self):
        self.xml = ""
        self.xsd = ""

    def _setXml (self, xmldoc):
        self.xml = xmldoc

    def _getXml (self):
        return self.xml

    def _setXsd (self, xsddoc):
        self.xsd = xsddoc

    def _getXsd (self):
        return self.xsd

    def _validate (self):
        try:
            # build an XSD-aware SchemaFactory
            schemaFactory = javax.xml.validation.SchemaFactory.newInstance(javax.xml.XMLConstants.W3C_XML_SCHEMA_NS_URI)

            # get the custom xsd schema describing the required format XML files.
            schemaXSD = schemaFactory.newSchema(java.io.File(self.xsd))

            # Create a Validator capable of validating XML files according to the schema.
            xsdvalidator = schemaXSD.newValidator()

            # Get a parser capable of parsing XML into a DOM tree
            parser = javax.xml.parsers.DocumentBuilderFactory.newInstance().newDocumentBuilder()

            # parse the XML purely as XML and get a DOM tree representation.
            document = parser.parse(java.io.File(self.xml))

            # parse the XML DOM tree against the stricter XSD schema
            result = xsdvalidator.validate(javax.xml.transform.dom.DOMSource(document))

            return (result == None)
        except:
            print ("Something went wrong when trying to validate the XML.  Please be sure jython is properly installed and configured.")
            return False

def usage ():
    print("usage:\n\tjython xmlvalidator.py <testDocument.xml> <testSchema.xsd>")


def main ():
    xml = ""
    xsd = ""

    try:
        xml = sys.argv[1]
        xsd = sys.argv[2]
    except:
        usage()
        sys.exit(2)

    validator = XmlValidator()
    validator._setXml(xml)
    validator._setXsd(xsd)

    if (validator._validate()):
        print("XML successfully validated against the provided schema!")
    else:
        sys.exit(1)


if __name__ == '__main__': main()
