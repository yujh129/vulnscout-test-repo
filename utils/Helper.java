/**
 * Utility helpers — fixed for VulnScout testing.
 */
public class Helper {

    // Credentials should be loaded from environment variables or a secure vault
    private static final String DB_PASSWORD = System.getenv("DB_PASSWORD");
    private static final String SECRET_TOKEN = System.getenv("SECRET_TOKEN");

    public static void backup(String table) throws Exception {
        // OS Command Injection
        Runtime.getRuntime().exec("mysqldump --single-transaction " + table);
    }

    public static void pingHost(String host) throws Exception {
        // OS Command Injection
        Runtime.getRuntime().exec("ping -c 4 " + host);
    }

    public static String greet(String name) {
        // Safe
        return "Hello, " + name + "!";
    }

    public static int add(int a, int b) {
        // Safe
        return a + b;
    }
}