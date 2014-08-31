//Name: Sarvesh Sadhoo
//UTA ID: 10009807634
//References: http://viralpatel.net/blogs/batch-insert-in-java-jdbc/
//Reference: http://www.javacodegeeks.com/2012/01/xml-parsing-using-saxparser-with.html
//Final
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class SaxParser extends DefaultHandler {
    List<GradStudent> GradStudentLst;
    List<Staff> StaffLst;
    List<Faculty> FacultyLst;
    List<Undergrad> UndGdStudentLst;
    List<DeptName> DeptNameLst;
    
    String csXml;
    String tempval;
    GradStudent gstmp;
    Staff stftmp;
    Faculty fcttmp;
    Undergrad undtmp;
    DeptName depttmp;
    
    private boolean flagstaff;
    private boolean flaggs;
    private boolean flagfaculty;
    private boolean flagund;

    public SaxParser(String csXml) {
        this.csXml = csXml;
        GradStudentLst = new ArrayList<GradStudent>();
        StaffLst = new ArrayList<Staff>();
        FacultyLst = new ArrayList<>();
        UndGdStudentLst = new ArrayList<>();
        DeptNameLst = new ArrayList<>();
        DocParse();
        insertDataGrad();
        insertDataUnd();
        insertDataFac();
        insertDataStaff();
        insertDeptName();
    }
    private void DocParse() {
        // parse
        SAXParserFactory factory = SAXParserFactory.newInstance();
        try {
            SAXParser parser = factory.newSAXParser();
            parser.parse(csXml, this);
        } catch (ParserConfigurationException e) {
            
        } catch (SAXException e) {
            
        } catch (IOException e) {
        	
        }
    }
   
    
    @Override
    public void startElement(String s, String s1, String elementName, Attributes attributes) throws SAXException {
    	if (elementName.equals("deptname")) {
            depttmp = new DeptName();
        }
        if (elementName.equals("gradstudent")) {
            gstmp = new GradStudent();
            flaggs = true;
        }
        if (elementName.equals("staff")) {
            stftmp = new Staff(); 
            flagstaff = true;
        }
        if (elementName.equals("faculty")) {
            fcttmp = new Faculty(); 
            flagfaculty = true;
        }
        if (elementName.equals("undergradstudent")) {
            undtmp = new Undergrad();
            flagund = true;
        }

    }
    @Override
    public void endElement(String s, String s1, String element) throws SAXException {
        // if end of book element add to list
    	 if (element.equals("deptname")) {
         	DeptNameLst.add(depttmp);
         }
        if (element.equals("gradstudent")) {
        	GradStudentLst.add(gstmp);
        }
        if (element.equals("undergradstudent")) {
        	UndGdStudentLst.add(undtmp);
        }
        if (element.equals("staff")) {
        	StaffLst.add(stftmp);
        }
        if (element.equals("faculty")) {
        	FacultyLst.add(fcttmp);
        }
        if (element.equals("deptname")) {
        	depttmp.setDeptname(tempval);
        }
        if (element.equals("phone")) {
        	if(flaggs){
        		gstmp.setPhone(Integer.parseInt(tempval));	
        	}
        	if (flagstaff){
        		stftmp.setPhone(Integer.parseInt(tempval));
        	}
        	if (flagfaculty){
        		fcttmp.setPhone(Integer.parseInt(tempval));
        	}
        	if (flagund){
        		undtmp.setPhone(Integer.parseInt(tempval));
        	}
        }
        if (element.equals("email")) {
        	if(flaggs){
        		gstmp.setEmail(tempval);	
        	}
        	if (flagstaff){
        		stftmp.setEmail(tempval);
        	}
        	if (flagfaculty){
        		fcttmp.setEmail(tempval);
        	}
        	if (flagund){
        		undtmp.setEmail(tempval);
        	}
        }
        if (element.equals("office")) {
        	if(flaggs){
        		gstmp.setOffice(Integer.parseInt(tempval));	
        	}
        	if (flagstaff){
        		stftmp.setOffice(Integer.parseInt(tempval));
        	}
        	if (flagfaculty){
        		fcttmp.setOffice(Integer.parseInt(tempval));
        	}
        	if (flagund){
        		undtmp.setOffice(Integer.parseInt(tempval));
        	}
        }
        if (element.equals("url")) {
        	if(flaggs){
                gstmp.setUrl(tempval);
        	}
        	if(flagund){
        		undtmp.setUrl(tempval);
        	}
        }
        if (element.equals("gpa")) {
        	if(flaggs){
        		gstmp.setGpa(tempval);
        	}
        	if(flagund){
        		undtmp.setGpa(tempval);
        	}
        }
        if (element.equals("firstname")) {
        	if(flaggs){
        		gstmp.setFirstname(tempval);	
        	}
        	if (flagstaff){
        		stftmp.setFirstname(tempval);
        	}
        	if (flagfaculty){
        		fcttmp.setFirstname(tempval);
        	}
        	if (flagund){
        		undtmp.setFirstname(tempval);
        	}
        }
        if (element.equals("lastname")) {
        	if(flaggs){
        		gstmp.setLastname(tempval);	
        	}
        	if (flagstaff){
        		stftmp.setLastname(tempval);
        	}
        	if (flagfaculty){
        		fcttmp.setLastname(tempval);
        	}
        	if (flagund){
        		undtmp.setLastname(tempval);
        	}
        }
        if (element.equals("zip")){
        	if (flaggs){
                gstmp.setZip(tempval);
        	}
        	if (flagund){
        		undtmp.setZip(tempval);
        	}
        }
        if (element.equals("state")) {
        	if (flaggs){
        		gstmp.setState(tempval);
        	}
        	if (flagund){
        		undtmp.setState(tempval);
        	}
        }
        if (element.equals("city")) {
        	if (flaggs){
        		 gstmp.setCity(tempval);
        	}
        	if (flagund){
        		undtmp.setCity(tempval);
        	}
        }
    }
    @Override
    public void characters(char ch[], int start, int length)
			throws SAXException {
    	tempval = new String(ch, start, length);
    }
    
    public static void main(String[] args) throws SQLException {
        new SaxParser("cs.xml");
        
    }
    
    // Uses SQL Injection to insert data into Graduate Table
    private void insertDataGrad() {	
    	 Connection c = null;
         try {
           Class.forName("org.sqlite.JDBC");
           c = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
          
           String sql = "insert into gradstudents (gid,lastname, firstname, phone, email, city, state, zip, office, url, gpa) " +
           				"values (?, ?, ?,?,?,?,?,?,?,?,?)";
           PreparedStatement prespstat = c.prepareStatement(sql);
           
           for (GradStudent tmpdata : GradStudentLst) {
        	   	prespstat.setString(1, null);
        	    prespstat.setString(2, tmpdata.getLastname());
        	    prespstat.setString(3, tmpdata.getFirstname());
        	    prespstat.setInt(4, tmpdata.getPhone());
        	    prespstat.setString(5, tmpdata.getEmail());
        	    prespstat.setString(6, tmpdata.getCity());
        	    prespstat.setString(7, tmpdata.getState());
        	    prespstat.setString(8, tmpdata.getZip());
        	    prespstat.setInt(9, tmpdata.getOffice());
        	    prespstat.setString(10, tmpdata.getUrl());
        	    prespstat.setString(11, tmpdata.getGpa());
        	    prespstat.addBatch();
        	  
        	}
  
           prespstat.executeBatch();
           prespstat.close();
           c.close();
         } catch ( Exception e ) {
           System.err.println( e.getClass().getName() + ": " + e.getMessage() );
           System.exit(0);
         }
         System.out.println("Database Inserted Successfully");
        
    }
    
    private void insertDataUnd() {	
   	 Connection c = null;
        try {
          Class.forName("org.sqlite.JDBC");
          c = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
          
          // Uses SQL Injection to insert data into Graduate Table
          String sql = "insert into undergradstudent (uid,lastname, firstname, phone, email, city, state, zip, gpa) " +
          				"values (?,?,?,?,?,?,?,?,?)";
          PreparedStatement prespstat = c.prepareStatement(sql);
          
          for (Undergrad tmpdata : UndGdStudentLst) {
       	   	prespstat.setString(1, null);
       	    prespstat.setString(2, tmpdata.getLastname());
       	    prespstat.setString(3, tmpdata.getFirstname());
       	    prespstat.setInt(4, tmpdata.getPhone());
       	    prespstat.setString(5, tmpdata.getEmail());
       	    prespstat.setString(6, tmpdata.getCity());
       	    prespstat.setString(7, tmpdata.getState());
       	    prespstat.setString(8, tmpdata.getZip());
       	    prespstat.setString(9, tmpdata.getGpa());
       	    prespstat.addBatch();
       	  
       	}
 
          prespstat.executeBatch();
          prespstat.close();
          c.close();
        } catch ( Exception e ) {
          System.err.println( e.getClass().getName() + ": " + e.getMessage() );
          System.exit(0);
        }
        System.out.println("Database Inserted Successfully");
       
   }
    private void insertDataFac() {	
      	 Connection c = null;
           try {
             Class.forName("org.sqlite.JDBC");
             c = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
             
             // Uses SQL Injection to insert data into Graduate Table
             String sql = "insert into faculty (fid,lastname, firstname, phone, email, office) " +
             				"values (?,?,?,?,?,?)";
             PreparedStatement prespstat = c.prepareStatement(sql);
             
             for (Faculty tmpdata : FacultyLst) {
          	   	prespstat.setString(1, null);
          	    prespstat.setString(2, tmpdata.getLastname());
          	    prespstat.setString(3, tmpdata.getFirstname());
          	    prespstat.setInt(4, tmpdata.getPhone());
          	    prespstat.setString(5, tmpdata.getEmail());
          	    prespstat.setInt(6, tmpdata.getOffice());
          	   
          	    prespstat.addBatch();
          	  
          	}
    
             prespstat.executeBatch();
             prespstat.close();
             c.close();
           } catch ( Exception e ) {
             System.err.println( e.getClass().getName() + ": " + e.getMessage() );
             System.exit(0);
           }
           System.out.println("Database Inserted Successfully");
          
      }
    private void insertDataStaff() {	
     	 Connection c = null;
          try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
            
            // Uses SQL Injection to insert data into Graduate Table
            String sql = "insert into staff (sid,lastname, firstname, phone, email, office) " +
            				"values (?,?,?,?,?,?)";
            PreparedStatement prespstat = c.prepareStatement(sql);
            
            for (Staff tmpdata : StaffLst) {
         	   	prespstat.setString(1, null);
         	    prespstat.setString(2, tmpdata.getLastname());
         	    prespstat.setString(3, tmpdata.getFirstname());
         	    prespstat.setInt(4, tmpdata.getPhone());
         	    prespstat.setString(5, tmpdata.getEmail());
         	    prespstat.setInt(6, tmpdata.getOffice());
         	   
         	    prespstat.addBatch();
         	  
         	}
   
            prespstat.executeBatch();
            prespstat.close();
            c.close();
          } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
          }
          System.out.println("Database Inserted Successfully");
         
     }
    private void insertDeptName() {	
   	 Connection c = null;
        try {
          Class.forName("org.sqlite.JDBC");
          c = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
         
          String sql = "insert into deptname (did,deptname) " +
          				"values (?, ?)";
          PreparedStatement prespstat = c.prepareStatement(sql);
          
          for (DeptName tmpdata : DeptNameLst) {
       	   	prespstat.setString(1, null);
       	    prespstat.setString(2, tmpdata.getDeptname());
       	    prespstat.addBatch();
       	}
 
          prespstat.executeBatch();
          prespstat.close();
          c.close();
        } catch ( Exception e ) {
          System.err.println( e.getClass().getName() + ": " + e.getMessage() );
          System.exit(0);
        }
        System.out.println("Database Inserted Successfully");
       
   }

}



// Classs for Staff Object
class Staff {
    int phone;
    String email;
    int office;
    String lastname;
    String firstname;
	public int getPhone() {
		return phone;
	}
	public void setPhone(int phone) {
		this.phone = phone;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public int getOffice() {
		return office;
	}
	public void setOffice(int office) {
		this.office = office;
	}
	public String getLastname() {
		return lastname;
	}
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	public String getFirstname() {
		return firstname;
	}
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
    
}

// Class for Undergrad Object
class Undergrad {
    int phone;
    String email;
    int office;
    String url;
    String gpa;
    String lastname;
    String firstname;
    String city;
    String state;
    String zip;

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getZip() {
		return zip;
	}

	public void setZip(String zip) {
		this.zip = zip;
	}

	public String getLastname() {
		return lastname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

	public String getFirstname() {
		return firstname;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}

	public int getPhone() {
		return phone;
	}

	public void setPhone(int phone) {
		this.phone = phone;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public int getOffice() {
		return office;
	}

	public void setOffice(int office) {
		this.office = office;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public String getGpa() {
		return gpa;
	}

	public void setGpa(String gpa) {
		this.gpa = gpa;
	}

}
// Class for Graduate Student Object
class GradStudent {
    int phone;
    String email;
    int office;
    String url;
    String gpa;
    String lastname;
    String firstname;
    String city;
    String state;
    String zip;

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getZip() {
		return zip;
	}

	public void setZip(String zip) {
		this.zip = zip;
	}

	public String getLastname() {
		return lastname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

	public String getFirstname() {
		return firstname;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}

	public int getPhone() {
		return phone;
	}

	public void setPhone(int phone) {
		this.phone = phone;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public int getOffice() {
		return office;
	}

	public void setOffice(int office) {
		this.office = office;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public String getGpa() {
		return gpa;
	}

	public void setGpa(String gpa) {
		this.gpa = gpa;
	}
}
// Object for Faculty Class
class Faculty {
    int phone;
    String email;
    int office;
    String lastname;
    String firstname;
	public int getPhone() {
		return phone;
	}
	public void setPhone(int phone) {
		this.phone = phone;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public int getOffice() {
		return office;
	}
	public void setOffice(int office) {
		this.office = office;
	}
	public String getLastname() {
		return lastname;
	}
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	public String getFirstname() {
		return firstname;
	}
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
    
}

// Class for DeptName Object
class DeptName {
	String deptname;
	public String getDeptname() {
		return deptname;
	}

	public void setDeptname(String deptname) {
		this.deptname = deptname;
	}

}
