package RecursiveThinking;

public class Main {

    public static int length(String str) {
        if (str.equals("")) {
            return 0;
        } else {
            return 1 + length(str.substring(1));
        }
    }

    public static void printChars(String str) {
        if (str.length() == 0) {
            return;
        } else {
            System.out.print(str.charAt(0));
            printChars(str.substring(1));
        }
    }

    public static void main(String[] args) {
        System.out.println(length("hiroo"));
        printChars("hiroo");
    }

}
