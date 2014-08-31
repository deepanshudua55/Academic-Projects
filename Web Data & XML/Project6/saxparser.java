// Name: Sarvesh Sadhoo
// UTA ID: 100980763
//Reference: http://www.beingjavaguys.com/2013/06/read-xml-file-with-sax-parser.html
// Final Version

import java.awt.List;
import java.util.ArrayList;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.ws.EndpointReference;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class saxparser extends DefaultHandler {

	private boolean volumestatus;
	private boolean numberstatus;
	private boolean authorstatus;
	private boolean titlestatus;
	private boolean articlestatus;
	private boolean articlesstatus;
	private boolean initstatus;
	private boolean endstatus;
	private boolean authorsstatus;
	private String volume;
	private String number;
	private String author;
	private String title;
	private String article;
	private String articles;
	private String authors;
	private String initPage;
	private String endPage;
	private int flag = 0;
	private int flag2 = 0;
	String tempValue = "";

	static ArrayList mainList = new ArrayList();
	Auth atr;
	Authrs atrs;
	ArrayList<Auth> authrList;
	ArrayList<Artc> artcList;
	Artc artc;

	public void startElement(String uri, String localName, String qName,
			Attributes attributes) throws SAXException {
		// System.out.println("Start Element :" + qName);
		if (qName.equals("volume")) {
			volumestatus = true;
		}
		if (qName.equals("number")) {
			numberstatus = true;
		}
		if (qName.equals("articles")) {
			articlesstatus = true;
			artcList = new ArrayList<Artc>();
		}
		if (qName.equals("article")) {
			artc = new Artc();
			articlestatus = true;
		}
		if (qName.equals("authors")) {
			atrs = new Authrs();
			authrList = new ArrayList<Auth>();
			authorsstatus = true;
		}
		if (qName.equals("author")) {
			atr = new Auth();
			authorstatus = true;
		}
		if (qName.equals("title")) {
			titlestatus = true;
		}
		if (qName.equals("initPage")) {
			initstatus = true;
		}
		if (qName.equals("endPage")) {
			endstatus = true;
		}

	}

	public void characters(char ch[], int start, int length)
			throws SAXException {

		tempValue = new String(ch, start, length);

		if (volumestatus) {
			this.volume = new String(ch, start, length);
			volumestatus = false;
		}
		if (numberstatus) {
			this.number = new String(ch, start, length);
			numberstatus = false;
		}
		if (articlesstatus) {
			this.articles = new String(ch, start, length);
			articlesstatus = false;
		}
		if (articlestatus) {
			this.article = new String(ch, start, length);
			articlestatus = false;
		}
		if (titlestatus) {
			this.title = new String(ch, start, length);
			titlestatus = false;
		}
		if (authorsstatus) {
			this.authors = new String(ch, start, length);
			authorsstatus = false;
			// System.out.println(authors);
		}
		if (authorstatus) {
			this.author = new String(ch, start, length);
			// authorstatus = false;
		}
		if (initstatus) {
			this.initPage = new String(ch, start, length);
			initstatus = false;

		}
		if (endstatus) {
			this.endPage = new String(ch, start, length);
			endstatus = false;
		}
		if (initPage != null && initPage.equals("26") && endPage.equals("54")) {
			flag = 1;
		}

		// ----------------Part
		// 1----------------------------------------------------

		ArrayList<String> output = new ArrayList<String>();
		if (volume.equals("13") && number.equals("4")
				&& author.equals("David Maier")) {
			output.add(title);
			titlestatus = true;
			System.out.println("--------------Part 1---------------------");
			for (String st : output) {
				
				System.out.println("Title: " + st);
			}

		}
		// ---------------- Part
		// 2---------------------------------------------------
		if (title != null
				&& (title.contains("Database") || title.contains("database"))) {
			// System.out.println(title);
			// System.out.println(authorstatus);

		}
		// ----------------Part
		// 3----------------------------------------------------
		if (flag == 1
				&& title != null
				&& title.equals("Research in Knowledge Base Management Systems.")) {
			System.out.println("---------Part 3 --------------------");
			System.out.println("Volume: " + volume);
			System.out.println("Number: " + number);
			System.out.println("Init Page: " + initPage);
			System.out.println("Init Page:" + endPage);
			titlestatus = true;

		}

	}

	public void endElement(String uri, String localName, String qName)
			throws SAXException {
		// System.out.println("End Element :" + qName);
		if (flag2 == 1 && qName == "author") {
			// System.out.println(flag2);
			System.out.println(author);
		}

		if (qName.equals("authors")) {
			atrs.setAuth(authrList);
			artc.setAthrs(atrs);
		}

		if (qName.equals("author")) {
			atr.setName(tempValue);
			authrList.add(atr);
		}

		if (qName.equals("title")) {
			artc.setTitle(tempValue);
		}

		if (qName.equals("article")) {
			artcList.add(artc);
		}

		if (qName.equals("articles")) {
			mainList.add(artcList);
		}

	}

	public static void main(String argv[]) {

		try {

			SAXParserFactory factory = SAXParserFactory.newInstance();
			SAXParser saxParser = factory.newSAXParser();

			saxParser.parse("SigmodRecord.xml", new saxparser());
			System.out.println("-----------------------Part 2---------------------------------");
			for (int i = 0; i < mainList.size(); i++) {
				ArrayList<Artc> aa = (ArrayList<Artc>) mainList.get(i);

				for (Artc a : aa) {
					if (a.getTitle().contains("database")
							|| a.getTitle().contains("Database")) {
						Authrs as = a.getAthrs();

						for (Auth at : as.getAuth()) {
							System.out.println("author :" + at.getName());
						}

					}
				}
			}

		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}

// DefaultHandler handler = new DefaultHandler() {};

class Artc {
	String title;

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public Authrs getAthrs() {
		return athrs;
	}

	public void setAthrs(Authrs athrs) {
		this.athrs = athrs;
	}

	Authrs athrs;
}

class Authrs {
	ArrayList<Auth> auth;

	public ArrayList<Auth> getAuth() {
		return auth;
	}

	public void setAuth(ArrayList<Auth> auth) {
		this.auth = auth;
	}

}

class Auth {
	String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
