// Name: Sarvesh Sadhoo
// UTA ID: 100980763


import javax.xml.xpath.*;
import org.xml.sax.InputSource;
import org.w3c.dom.*;

class xpath {

    static void print ( Node e ) {
	if (e instanceof Text)
	    System.out.print(((Text) e).getData());
	else {
	    NodeList c = e.getChildNodes();
	    System.out.print("<"+e.getNodeName());
	    NamedNodeMap attributes = e.getAttributes();
	    for (int i = 0; i < attributes.getLength(); i++)
		System.out.print(" "+attributes.item(i).getNodeName()
				 +"=\""+attributes.item(i).getNodeValue()+"\"");
	    System.out.print(">");
	    for (int k = 0; k < c.getLength(); k++)
		print(c.item(k));
	    System.out.print("</"+e.getNodeName()+">");
	}
    }

    static void eval ( String query, String document ) throws Exception {
	XPathFactory xpathFactory = XPathFactory.newInstance();
	XPath xpath = xpathFactory.newXPath();
	InputSource inputSource = new InputSource(document);
	NodeList result = (NodeList) xpath.evaluate(query,inputSource,XPathConstants.NODESET);
	for (int i = 0; i < result.getLength(); i++)
	    System.out.println(result.item(i).getNodeName() + ": " + result.item(i).getTextContent());
    }

    public static void main ( String[] args ) throws Exception {
    	System.out.println("-------------------Part 1---------------------------------------------------------------");
    	String xPathExp1 = ("//*/issue[volume=13 and number=4]/articles/article[authors/author='David Maier']/title");
    	eval(xPathExp1,"SigmodRecord.xml");
    	System.out.println("-------------------Part 2---------------------------------------------------------------");
    	String xPathQuery2 = ("//*/issue/articles/article[contains(substring(./title,2), 'atabase')]/authors/author");
    	eval(xPathQuery2,"SigmodRecord.xml");
    	System.out.println("-------------------Part 3---------------------------------------------------------------");
    	String initPage = ("/*/issue/articles/article/title[contains(text(),'Research in Knowledge Base Management Systems')]/../initPage");
    	String endPage = ("/*/issue/articles/article/title[contains(text(),'Research in Knowledge Base Management Systems')]/../endPage");
    	String volume = ("/*/issue/articles/article/title[contains(text(),'Research in Knowledge Base Management Systems')]/../../../volume");
    	String number = ("/*/issue/articles/article/title[contains(text(),'Research in Knowledge Base Management Systems')]/../../../number");
    	eval(initPage + "|" + endPage +"|" + volume + "|" + number,"SigmodRecord.xml");
    	
    }
}