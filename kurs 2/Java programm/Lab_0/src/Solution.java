public class Solution {
    public static void main(String[] args) {
        print("The power is easy to use!");
        print("The power opens many opportunities!");
        increaseSpeed(700);
        Zam zam = new Zam();
        Dron dron = new Dron();

        zam.spy = dron;
        dron.hunter = zam;

        System.out.println("zam.spy: " + zam.spy);
        System.out.println("dron.hunter: " + dron.hunter);
        Jedi jedi1 = new Jedi();
        jedi1.name = "Obi-Wan";

        Jedi jedi2 = new Jedi();
        jedi2.name = "Anakin";

        Jedi jedi3 = new Jedi();
        jedi3.name ="Joda";

        Clone clone1 = new Clone();
        Clone clone2 = new Clone();
        Clone clone3 = new Clone();
        Clone clone4 = new Clone();
        Clone clone5 = new Clone();
        Clone clone6 = new Clone();
        Clone clone7 = new Clone();
        Clone clone8 = new Clone();
        Clone clone9;
        Clone clone10;

        Clone1 clone111 = new Clone1();
        Clone2 clone222 = new Clone2();
        Clone3 clone333 = new Clone3();
        Dias dias = new Dias();
        clone111.owner = dias;
        clone222.owner = dias;
        clone333.owner = dias;

        System.out.println(getWeight(888));

        print3("Help me!");

        System.out.println(min(12, 33));
        System.out.println(min(-20, 0));
        System.out.println(min(-10, -20));
    }

    public static int min(int a, int b) {
        if (a < b){
            return a;
        } else {
            return b;
        }
    }

    public static void print3(String s) {
        System.out.println(s + " " + s + " " + s + " ");
    }


    public static double getWeight(int weight) {
        weight=weight/6;
        return weight;
    }
    public static class Clone1 {
        public Dias owner;
    }
    public static class Clone2 {
        public Dias owner;
    }
    public static class Clone3 {
        public Dias owner;
    }
    public static class Dias {
    }

    public static class Clone {
    }

    public static class Jedi {
        public String name;
    }


    public static class Zam {
        public int x = 10;
        public int y = 20;
        public int z = 30;
        Dron spy;
    }

    public static class Dron {
        public int a = 1;
        public int b = 2;
        public int c = 3;
        public Zam hunter;
    }

    public static void increaseSpeed(int s){
        System.out.println("Your speed is: " + (s + 100) + " km/h.");
    }


    public static void print(String s) {
        for (int i = 1; i < 5; i++) {
            System.out.println(s);
        }
    }
}