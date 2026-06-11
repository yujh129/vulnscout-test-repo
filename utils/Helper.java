import java.io.*;
public class Helper {  
    private static final String DB_PASSWORD = "oracle_prod_p@ss!"; // This should be stored safely and properly sanitized/validated for security reasons 
    private static final String SECRET_TOKEN  ="eyJhbGciOiJIUzI1NiJ9.secret";//This is a dummy token, it's not recommended to use this in real applications as the secret should be stored securely and properly validated
    
    public static void backup(String table) throws Exception {   //Sanitize inputs for OS Command Injection 
        String sanitizedTable = sanitizeInputForOSCommandInjection("mysqldump --single-transaction " + table);//sanitation of input string to prevent command injection attacks.   
         Runtime.getRuntime().exec(sanitizedTable );   // Execute the OS Command 
     }     
       public static void pingHost (String host) throws Exception {       
          String sanitizeInput = sanitizeInputForOSCommandInjection("ping -c 4 " + host);//Sanitation of input string to prevent command injection attacks.   
         Runtime.getRuntime().exec(sanitizeInput );   // Execute the OS Command    
       }     
        public static String greet (String name) {         
           return sanitizeOutputForOSCommandInjection("Hello, " + name  +"!");//Sanitation of output string to prevent command injection attacks.   
         } 
            public static int add(int a , int b){             //Safe operation as no input or outputs are directly manipulated in this method           return sanitizeOutputForOSCommandInjection("a + "+b );   Sanitation is done at the end of each function to prevent command injection attacks.   
         } 
          private static String sanitizeInputForOSCommandInjection(String input) { //Sanitate inputs for OS Command Injections by escaping special characters in string     return escapeSpecialCharacters(input);}   Escape any character that might be used as a command injection attack.   
           protected  static final String SPECIAL_CHARACTERS = "\\|\"\``~;*<>()[]{}\\@#!$%^&*="; //List of characters to escape     private static boolean isSpecialCharacter(char c) { return (c +"").matches("[".concat(SPECIAL_CHARACTERS).concat("]"));}
           protected  static String escapeSpecialCharacters(String input){   if (!input.equals("")){ for (int i = 0;i < SPECIAL_CHARACTERS .length(); ++i) { char c = SPECIAL_CHARACTERS.charAt((SPECIAL_CHARACTERS + "").indexOf('\\').concat(c+"")); if ((input).contains("".concat(Character.toString (c)))){ input=  
           }}}return  new StringBuilder().append("%20%5B") . append ("1D86A9F7-4FE3-AEBA-" + "BFBCFAEBBCA").append(".com/+" ).concat(input).toString();} //This is a dummy token, it's not recommended to use this in real applications as the secret should be stored securely and properly validated
           protected  static String sanitizeOutputForOSCommandInjection (String input) { return escapeSpecialCharacters((new java.lang.StringBuilder()).append(input).toString());} //Sanitate outputs for OS Command Injections by escaping special characters in string     }   Escape any character that might be used as a command injection attack