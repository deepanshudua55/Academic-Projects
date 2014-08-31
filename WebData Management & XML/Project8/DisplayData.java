//Name: Sarvesh Sadhoo
//UTA ID: 10009807634
//References: http://www.tutorialspoint.com/sqlite/sqlite_java.htm
//References: http://www.javacodegeeks.com/2012/01/xml-parsing-using-saxparser-with.html
//Final
import java.sql.*;

public class DisplayData{
	
	private void getdptnameydata(){
		Connection cnct = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      cnct = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
	      cnct.setAutoCommit(false);

	      stmt = cnct.createStatement();
	      ResultSet rsltst = stmt.executeQuery( "SELECT * FROM deptname;" );
	      while ( rsltst.next() ) {
	         String  deptname = rsltst.getString("deptname");	     ;
	         System.out.println("<deptname>" + deptname +"</deptname>");
	   
	      }
	      rsltst.close();
	      stmt.close();
	      cnct.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
  }
	private void getgraddata(){
		Connection cnct = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      cnct = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
	      cnct.setAutoCommit(false);

	      stmt = cnct.createStatement();
	      ResultSet rsltst = stmt.executeQuery( "SELECT * FROM gradstudents;" );
	      while ( rsltst.next() ) {
	    	 
	         int gid = rsltst.getInt("gid");
	         String  lastname = rsltst.getString("lastname");
	         String  firstname = rsltst.getString("firstname");
	         int phone  = rsltst.getInt("phone");
	         String  email = rsltst.getString("email");
	         String city = rsltst.getString("city");
	         String state = rsltst.getString("state");
	         String zip = rsltst.getString("zip");
	         int office = rsltst.getInt("office");
	         String url = rsltst.getString("url");
	         String gpa = rsltst.getString("gpa");
	         
	         System.out.println("<gradstudent>");
	         System.out.println("<name>");
	         System.out.println("<lastname>" +lastname +"</lastname>");
	         System.out.println("<firstname>" +firstname +"</firstname>");
	         System.out.println("</name>");
	         System.out.println("<phone>" + phone +"</phone>");
	         System.out.println("<email>" + email +"</email>");
	         System.out.println("<address>");
	         System.out.println("<city>"+ city + "</city>");
	         System.out.println("<state>"+ state + "</state>");
	         System.out.println("<zip>"+ zip + "</zi>");
	         System.out.println("</address>");
	         System.out.println("<office>"+ office + "</office>");
	         System.out.println("<url>"+ url + "</url>");
	         System.out.println("<gpa>"+ gpa + "</gpa>");
	      }
	      rsltst.close();
	      stmt.close();
	      cnct.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
  }
	private void getunddata(){
		Connection cnct = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      cnct = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
	      cnct.setAutoCommit(false);

	      stmt = cnct.createStatement();
	      ResultSet rsltst = stmt.executeQuery( "SELECT * FROM undergradstudent;" );
	      while ( rsltst.next() ) {
	    	 
	         int gid = rsltst.getInt("uid");
	         String  lastname = rsltst.getString("lastname");
	         String  firstname = rsltst.getString("firstname");
	         int phone  = rsltst.getInt("phone");
	         String  email = rsltst.getString("email");
	         String city = rsltst.getString("city");
	         String state = rsltst.getString("state");
	         String zip = rsltst.getString("zip");
	         String gpa = rsltst.getString("gpa");
	         
	         System.out.println("<undergradstudent>");
	         System.out.println("<name>");
	         System.out.println("<lastname>" +lastname +"</lastname>");
	         System.out.println("<firstname>" +firstname +"</firstname>");
	         System.out.println("</name>");
	         System.out.println("<phone>" + phone +"</phone>");
	         System.out.println("<email>" + email +"</email>");
	         System.out.println("<address>");
	         System.out.println("<city>"+ city + "</city>");
	         System.out.println("<state>"+ state + "</state>");
	         System.out.println("<zip>"+ zip + "</zi>");
	         System.out.println("</address>");
	         System.out.println("<gpa>"+ gpa + "</gpa>");
	         System.out.println("</undergradstudent>");
	      }
	      rsltst.close();
	      stmt.close();
	      cnct.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
  }
	
	private void getstaffdata(){
		Connection cnct = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      cnct = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
	      cnct.setAutoCommit(false);

	      stmt = cnct.createStatement();
	      ResultSet rsltst = stmt.executeQuery( "SELECT * FROM staff;" );
	      while ( rsltst.next() ) {
	    	 
	         String  lastname = rsltst.getString("lastname");
	         String  firstname = rsltst.getString("firstname");
	         int phone  = rsltst.getInt("phone");
	         String  email = rsltst.getString("email");
	         int office = rsltst.getInt("office");
	         
	         System.out.println("<staff>");
	         System.out.println("<name>");
	         System.out.println("<lastname>" +lastname +"</lastname>");
	         System.out.println("<firstname>" +firstname +"</firstname>");
	         System.out.println("</name>");
	         System.out.println("<phone>" + phone +"</phone>");
	         System.out.println("<email>" + email +"</email>");
	         System.out.println("<office>"+ office + "</office>");
	         System.out.println("</staff>");
	      }
	      rsltst.close();
	      stmt.close();
	      cnct.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
  }
	private void getfacultydata(){
		Connection cnct = null;
	    Statement stmt = null;
	    try {
	      Class.forName("org.sqlite.JDBC");
	      cnct = DriverManager.getConnection("jdbc:sqlite:C:/Users/SRV/Desktop/project8");
	      cnct.setAutoCommit(false);

	      stmt = cnct.createStatement();
	      ResultSet rsltst = stmt.executeQuery( "SELECT * FROM faculty;" );
	      while ( rsltst.next() ) {
	    	 
	         String  lastname = rsltst.getString("lastname");
	         String  firstname = rsltst.getString("firstname");
	         int phone  = rsltst.getInt("phone");
	         String  email = rsltst.getString("email");
	         int office = rsltst.getInt("office");
	         
	         System.out.println("<faculty>");
	         System.out.println("<name>");
	         System.out.println("<lastname>" +lastname +"</lastname>");
	         System.out.println("<firstname>" +firstname +"</firstname>");
	         System.out.println("</name>");
	         System.out.println("<phone>" + phone +"</phone>");
	         System.out.println("<email>" + email +"</email>");
	         System.out.println("<office>"+ office + "</office>");
	         System.out.println("</faculty>");
	      }
	      rsltst.close();
	      stmt.close();
	      cnct.close();
	    } catch ( Exception e ) {
	      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
	      System.exit(0);
	    }
  }
  public static void main( String args[] ){
	  System.out.println("<department>");
	  DisplayData objct = new DisplayData();
	  objct.getdptnameydata();
	  System.out.println("");
	  objct.getgraddata();
	  System.out.println("");
	  objct.getstaffdata();
	  System.out.println("");
	  objct.getfacultydata();
	  System.out.println("");
	  objct.getunddata();
	  System.out.println("<department>");
  }
}