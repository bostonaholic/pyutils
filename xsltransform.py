'''
Created on Jan 4, 2010

@author: mboston
@attention: This is a Jython script and must be compiled and run with Jython
'''

import sys
try:
    from java.io import FileInputStream
    from java.io import ByteArrayOutputStream
    from javax.xml.transform import TransformerFactory
    from javax.xml.transform.stream import StreamSource
    from javax.xml.transform.stream import StreamResult
except ImportError:
    print("Unable to import the Java libraries.  Be sure you have Jython installed.")
    sys.exit(2)

class XslTransform ():
    sourceXml = None
    xsl = None
    targetXml = None

    def __init__(self):
        self.sourceXml = ""
        self.xsl = ""
        self.targetXml = ""

    def _setSourceXml(self, xml):
        self.sourceXml = xml

    def _setXsl(self, xsl):
        self.xsl = xsl

    def _setTargetXml(self, xml):
        self.targetXml = xml

    def _transform(self):
        try:
            input = FileInputStream(self.xsl)
            xslSource = StreamSource(input)
            xslTemplate = TransformerFactory.newInstance().newTemplates(xslSource);
            transformer = xslTemplate.newTransformer()

            output = ByteArrayOutputStream()
            result = StreamResult(output)

            source = StreamSource(FileInputStream(self.sourceXml))
            transformer.transform(source, result)

            f = open(self.targetXml, 'w')
            f.write(output.toString())

            return True
        except:
            print ("Something went wrong when trying to transform the XML.  Please be sure jython is properly installed and configured.")
            return False

def usage ():
    print("usage:\n\tjython xsltransform.py <source.xml> <transform.xsl> [<target.xml>]")
    print("\tIf <target.xml> is not specified, the transformed XML will be written to <source.xml>")

def main ():
    sourceXml = ""
    xsl = ""
    targetXml = ""

    try:
        sourceXml = sys.argv[1]
        xsl = sys.argv[2]
        if (len(sys.argv) == 4):
            targetXml = sys.argv[3]
        else:
            targetXml = sourceXml
    except:
        usage()
        sys.exit(2)

    xt = XslTransform()
    xt._setSourceXml(sourceXml)
    xt._setXsl(xsl)
    xt._setTargetXml(targetXml)

    if(xt._transform()):
        print("The document was successfully transformed!")
    else:
        sys.exit(1)

if __name__ == '__main__': main()
