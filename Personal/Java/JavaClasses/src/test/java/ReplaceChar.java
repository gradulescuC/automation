public class ReplaceChar {

    public static void main(String[] args) {
        String original = "alabala portocala";
        String nou = original.charAt(0)+ original.substring(1,original.length()-1).replace(original.charAt(0),Character.toUpperCase(original.charAt(0)))+original.charAt(0);
        System.out.println(nou);

    }
}
