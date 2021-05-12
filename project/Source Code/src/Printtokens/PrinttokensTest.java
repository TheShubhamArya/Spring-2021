package Printtokens;

import static org.junit.jupiter.api.Assertions.*;


import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.io.Reader;
import java.io.StringReader;

import org.junit.jupiter.api.Test;

import com.sun.tools.javac.Main;

class PrinttokensTest {
	
	@Test
	void is_token_end_test() {
		assertEquals(true,Printtokens.is_token_end(0,-1));
		assertEquals(true,Printtokens.is_token_end(1,9));
		assertEquals(true,Printtokens.is_token_end(1,13));
		assertEquals(true,Printtokens.is_token_end(1,10));
		assertEquals(false,Printtokens.is_token_end(1,65));
		assertEquals(true,Printtokens.is_token_end(2,13));
		assertEquals(true,Printtokens.is_token_end(2,10));
		assertEquals(false,Printtokens.is_token_end(2,65));
		assertEquals(true,Printtokens.is_token_end(3,40));
		assertEquals(true,Printtokens.is_token_end(3,13));
		assertEquals(true,Printtokens.is_token_end(3,10));
		assertEquals(true,Printtokens.is_token_end(3,59));
		assertEquals(true,Printtokens.is_token_end(3,32));
		assertEquals(false,Printtokens.is_token_end(3,65));
	}
	
	@Test
	void is_keyword_test() {
		assertEquals(true,Printtokens.is_keyword("and"));
		assertEquals(true,Printtokens.is_keyword("or"));
		assertEquals(true,Printtokens.is_keyword("if"));
		assertEquals(true,Printtokens.is_keyword("xor"));
		assertEquals(true,Printtokens.is_keyword("lambda"));
		assertEquals(true,Printtokens.is_keyword("=>"));
		assertEquals(false,Printtokens.is_keyword("nor"));
	}
	
	@Test
	void is_num_constant_test() {
		assertEquals(false,Printtokens.is_num_constant("ok"));
		assertEquals(false,Printtokens.is_num_constant("1ok"));
		assertEquals(true,Printtokens.is_num_constant("123"));
		assertEquals(true,Printtokens.is_num_constant("123\0"));
		
	}
	
	@Test
	void is_str_constant_test() {
		assertEquals(false,Printtokens.is_str_constant("and"));
		assertEquals(true,Printtokens.is_str_constant("\"\""));
		assertEquals(false,Printtokens.is_str_constant("\"hello"));
		assertEquals(false,Printtokens.is_str_constant("\"hello\0"));
	}
	
	@Test
	void is_identifier_test() {
		assertEquals(false,Printtokens.is_identifier("123"));
		assertEquals(true,Printtokens.is_identifier("a1b3"));
		assertEquals(false ,Printtokens.is_identifier("aa@#"));
		assertEquals(true,Printtokens.is_identifier("a123\0"));
	}
	
	@Test
	void is_char_constant() {
		assertEquals(true,Printtokens.is_char_constant("#a"));
		assertEquals(false,Printtokens.is_char_constant("#1"));
		assertEquals(false,Printtokens.is_char_constant("a"));
		assertEquals(false,Printtokens.is_char_constant("ab"));
		assertEquals(false,Printtokens.is_char_constant("12"));
		assertEquals(false,Printtokens.is_char_constant("#12"));
	}

	@Test 
	void get_token_test() {
		
		Printtokens tok = new Printtokens();
		
		//[1,2,3,4]
		Reader input = new StringReader("");
		BufferedReader br = new BufferedReader(input);
		assertEquals(null,tok.get_token(br));
		
		//[1,2,3,5,6,7,8,6,9,10]
		Reader input21 = new StringReader("\t");
		BufferedReader br21 = new BufferedReader(input21);
		assertEquals(null,tok.get_token(br21));
		
		//[1,2,3,5,6,7,8,6,9,10]
		Reader input22 = new StringReader("\n");
		BufferedReader br22 = new BufferedReader(input22);
		assertEquals(null,tok.get_token(br22));
		
		//[1,2,3,5,6,7,8,6,9,10]
		Reader input23 = new StringReader("\r");
		BufferedReader br23 = new BufferedReader(input23);
		assertEquals(null,tok.get_token(br23));
		
		//[1,2,3,5,6,9,11,12,13]
		Reader input3 = new StringReader(")");
		BufferedReader br3 = new BufferedReader(input3);
		assertEquals(")",tok.get_token(br3));
	
		//[1,2,3,5,6,9,11,12,14,15,16,18,19,20,21]
		Reader input4 = new StringReader("\"");
		BufferedReader br4 = new BufferedReader(input4);
		assertEquals("\"",tok.get_token(br4));
		
		//[1,2,3,5,6,9,11,12,14,16,17,18,19,20,21]
		Reader input5 = new StringReader(";");
		BufferedReader br5 = new BufferedReader(input5);
		assertEquals(";",tok.get_token(br5));
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,24,25,26,28,23,29,30,31]
		Reader input6 = new StringReader("hello");
		BufferedReader br6 = new BufferedReader(input6);
		assertEquals("hello",tok.get_token(br6));
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,24,25,26,27,29,32,33,34]
		Reader input7 = new StringReader("hello[");
		BufferedReader br7 = new BufferedReader(input7);
		assertEquals("hello",tok.get_token(br7)); 						
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,29,32,35,36,38]
		Reader input8 = new StringReader("\"hello\"");
		BufferedReader br8 = new BufferedReader(input8);
		assertEquals("\"hello\"",tok.get_token(br8));
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,29,32,35,36,37,38]
		Reader input9 = new StringReader("\"hello");
		BufferedReader br9 = new BufferedReader(input9);
		assertEquals("\"hello",tok.get_token(br9));
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,29,32,35,39,40,41]
		Reader input10 = new StringReader("hello;"); 
		BufferedReader br10 = new BufferedReader(input10);
		assertEquals("hello",tok.get_token(br10));
		
		//[1,2,3,5,6,9,11,12,14,16,18,19,22,23,29,32,35,39,42]
		Reader input11 = new StringReader("\";\"hello");
		BufferedReader br11 = new BufferedReader(input11);
		assertEquals("\";\"",tok.get_token(br11));
		
	}
	
	
	@Test
	void main_test() throws IOException{
		
		PrintStream stdout = System.out;
		InputStream stdin = System.in;
		
		//[1,3,5]
		ByteArrayOutputStream actual_output = new ByteArrayOutputStream();
		System.setOut(new PrintStream(actual_output));
		String[] args2 = {"src/main_test.txt","too many arguments"};
		Printtokens.main(args2);
		assertEquals("Error! Please give the token stream\n", actual_output.toString());
		
		//[1,2,6,7,8,9,12]
		actual_output = new ByteArrayOutputStream();	
		System.setOut(new PrintStream(actual_output));
		Printtokens.main(new String[] {"src/main_test.txt"});
		assertEquals("error,\"/hello\".\n"
				+ "identifier,\"world\".\n"
				+ "rsquare.\n"
				+ "bquote.\n"
				+ "quote.\n", actual_output.toString()); 
		
		//[1,3,4,7,8,9,10,11,9,12]
		actual_output = new ByteArrayOutputStream();
		System.setOut(new PrintStream(actual_output));
		ByteArrayInputStream input = new ByteArrayInputStream(";abc".getBytes()); 
		System.setIn(input);
		Printtokens.main(new String[] {});
		assertEquals("comment,\";abc\".\n", actual_output.toString());
		
		System.setOut(stdout);
		System.setIn(stdin);
	}
	
	
	@Test
	void end_to_end_test() throws IOException{
		
		PrintStream stdout = System.out;
		InputStream stdin = System.in;
		
		
		ByteArrayOutputStream actual_output = new ByteArrayOutputStream();
		System.setOut(new PrintStream(actual_output));
		String[] args2 = {"src/end_to_end_test.txt","too many arguments"};
		Printtokens.main(args2);
		assertEquals("Error! Please give the token stream\n", actual_output.toString());
		
		
		actual_output = new ByteArrayOutputStream();	 
		System.setOut(new PrintStream(actual_output));
		Printtokens.main(new String[] {"src/end_to_end_file.txt"});
		assertEquals("keyword,\"and\".\n"
				+ "keyword,\"or\".\n"
				+ "keyword,\"if\".\n"
				+ "keyword,\"xor\".\n"
				+ "keyword,\"lambda\".\n"
				+ "keyword,\"=>\".\n"
				+ "identifier,\"nand\".\n"
				+ "lsquare.\n"
				+ "string,\"123\".\n"
				+ "rsquare.\n"
				+ "error,\"’\".\n"
				+ "bquote.\n"
				+ "string,\"\".\n"
				+ "string,\")\".\n"
				+ "identifier,\"a12\".\n"
				+ "error,\"a12\\0\".\n"
				+ "identifier,\"a1b3\".\n"
				+ "error,\"aa@#\".\n"
				+ "error,\"12a\".\n"
				+ "numeric,123.\n"
				+ "string,\"123\\0\".\n"
				+ "string,\"Hello\".\n"
				+ "string,\"world\\0\".\n"
				+ "error,\"\"Wow\".\n"
				+ "character,\"a\".\n"
				+ "error,\"#1\".\n"
				+ "error,\"#abc\".\n"
				+ "comment,\";hello\".\n"
				+ "error,\"/hello\".\n"
				+ "error,\"“hello\".\n"
				+ "comment,\";”\".\n"
				+ "error,\"“\".\n"
				+ "comment,\";”hello”\".\n"
				+ "string,\";\".\n"
				+ "string,\"hello[\".\n"
				+ "comment,\";hello\\n\".\n"
				+ "comment,\";hello\\r\".\n"
				+ "comment,\";hello\\t\".\n"
				+ "lparen.\n"
				+ "string,\"hello\".\n"
				+ "rparen.\n", actual_output.toString()); 
		
		
		actual_output = new ByteArrayOutputStream();
		System.setOut(new PrintStream(actual_output));
		ByteArrayInputStream input = new ByteArrayInputStream("'".getBytes()); 
		System.setIn(input);
		Printtokens.main(new String[] {});
		assertEquals("quote.\n", actual_output.toString());
		
		System.setOut(stdout);
		System.setIn(stdin);
		
		
	}
}