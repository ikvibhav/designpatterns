package custom_java_packages.singleton;

public class Main {
    public static void main(String[] args) {
        Singleton singletonInstance = Singleton.getInstance();
        System.out.println("Singleton instance: " + singletonInstance);
    }
}