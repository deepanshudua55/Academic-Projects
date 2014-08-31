// Name: Sarvesh Sadhoo
// UTA ID: 100980763
// References: https://www.youtube.com/watch?v=q-oQ5D91TAk

import org.w3c.dom.*;
import javax.xml.parsers.*;

public class domparser{
	
	public static void main(String[] args){
		System.out.println("--------Part 1-------------------------------");
		Document xmlDoc = getDocument("SigmodRecord.xml");
		int issue_length = xmlDoc.getElementsByTagName("issue").getLength();
		NodeList issue_node =  xmlDoc.getElementsByTagName("issue");
		
		
		for(int i = 0; i < issue_length ; i++){
			Node nnode=issue_node.item(i);
			if(nnode.getNodeType() == Element.ELEMENT_NODE){
				Element enode =(Element)nnode;
				String vol_element = enode.getElementsByTagName("volume").item(0).getTextContent();
				String num_element = enode.getElementsByTagName("number").item(0).getTextContent();
				if(vol_element.equals("13") && num_element.equals("4")){
					NodeList article_node = xmlDoc.getElementsByTagName("article");
					int article_length = xmlDoc.getElementsByTagName("article").getLength();
					for(int j = 0; j < article_length; j++){
						Node m=article_node.item(j);
						if(m.getNodeType() == Element.ELEMENT_NODE){
							Element f = (Element)m;
							String auth = f.getElementsByTagName("author").item(0).getTextContent();
							if(auth.equals("David Maier")){
								String title = f.getElementsByTagName("title").item(0).getTextContent();
								System.out.println("Title: " + title);	
							}		
						}	
					}	
				}	
			}
		}
		//Part 2 of the Program (Print the author names off all articles whose title contains the word "database" or "Database".)
		System.out.println("--------Part 2------------------------------- ");
		NodeList article_node = xmlDoc.getElementsByTagName("article");
		int article_length = xmlDoc.getElementsByTagName("article").getLength();
		for(int j = 0; j < article_length; j++){
			Node m=article_node.item(j);
			if(m.getNodeType() == Element.ELEMENT_NODE){
				Element f = (Element)m;
				String article = f.getElementsByTagName("title").item(0).getTextContent();
				if( article.contains("Database") ||article.contains("database")){
					int length = f.getElementsByTagName("author").getLength();
					for(int i=0;i<length;i++){
						String auth = f.getElementsByTagName("author").item(i).getTextContent();
						System.out.println("Author: " + auth);
					}
				}
			}
		}
		//Part 3 of the Program (Print the volume/number and the init/end pages of the article titled "Research in Knowledge Base Management Systems.".)
		System.out.println("--------Part 3------------------------------- ");
		vol(issue_length,issue_node);
		
	}
	
	
	public static void vol(int issue_length,NodeList issue_node){
		for(int i = 0; i < issue_length ; i++){
			Node nnode=issue_node.item(i);
			if(nnode.getNodeType() == Element.ELEMENT_NODE){
				Element enode =(Element)nnode;
				 
					NodeList article_node = enode.getElementsByTagName("article");
					int article_length = enode.getElementsByTagName("article").getLength();
					
					for(int j = 0; j < article_length; j++){
						Node m=article_node.item(j);
						if(m.getNodeType() == Element.ELEMENT_NODE){
							Element f = (Element)m;
							String title = f.getElementsByTagName("title").item(0).getTextContent();
							//System.out.println(title);
							if(title.equals("Research in Knowledge Base Management Systems.")){
								//String article = f.getElementsByTagName("title").item(0).getTextContent();
								String endPage = f.getElementsByTagName("endPage").item(0).getTextContent();
					            String initPage = f.getElementsByTagName("initPage").item(0).getTextContent();
				            	String vol_element = enode.getElementsByTagName("volume").item(0).getTextContent();
					            String num_element = enode.getElementsByTagName("number").item(0).getTextContent();
					        	//System.out.println("Title: "+ title);
					            System.out.println("Volume: " + vol_element);
					            System.out.println("Number: " + num_element);
								System.out.println("Init Page: " + initPage);
								System.out.println("End Page: "+ endPage);
					            
				            }
									
						}	
					}	
					
			}
		}
	}
	
	private static Document getDocument(String docString) {
		try{ 
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			
			factory.setIgnoringComments(true);
			factory.setIgnoringElementContentWhitespace(true);
			factory.setValidating(true);
			
			DocumentBuilder builder = factory.newDocumentBuilder();
			
			return builder.parse(docString);
				
		}
		
		catch(Exception ex) {
			System.out.println(ex.getMessage());
		}
		return null;
	}
}