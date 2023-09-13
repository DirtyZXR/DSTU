// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static int a = 1;
    public static int b = 3;
    public static int c = 9;
    public static int d = 27;

    public static void main(String[] args) {
        // Press Alt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it
        String jedi = "Hello world";
        System.out.printf("%s\n", jedi);

        int number=2;
        Integer.toString(number);//TODO как работает преобразование строк
        System.out.println(number*number);

        for (int i = 1; i <11; i++){
            System.out.println("May the Force be with you.\n");
        }
        String s = "Anakin ";
        System.out.print(s);
        /*System.out.println("how are you? ");
        System.out.println("I am ");
        System.out.println("glad ");
        System.out.print("to see you.");
        System.out.println("This Lightsaber ");*/
        System.out.print("is ");
        //System.out.print("Your");
        System.out.print("a hero");
        System.out.println("!");

        String mol = "Mol";
        String text = "Darth " + mol + "!";
        System.out.println(text);

        int result = -a + b - c + d;
        System.out.println(result);

        System.out.println(sqr(5));

        //int a = 1;
        double b = 1.5;
        double c = b + 1.5;
        //int d = a + 12;
        //double e = 12.3;
        // String s = "Luke, " + a;
        String s1 = "Twice ";
        //String s2 = "a";
        String s3 = s1 + "the pride, ";
        String s4 = " the fall.";
        System.out.println(s3 + c + s4);
    }
    public static int sqr(int a){
        return a*a;



    }
}