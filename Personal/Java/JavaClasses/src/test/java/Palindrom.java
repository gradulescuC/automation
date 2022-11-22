public class Palindrom {
    public static void main(String[] args) {

        String pali = "123456";
        String rev="";
        char chr;
        for (int i=0; i<pali.length(); i++){
            chr = pali.charAt(i);
            rev= chr+ rev;
        }
        if (pali.equals(rev)){
            System.out.println("Este palindrom");
        }else{
            System.out.println("Nu este palindrom");
        }


    }
}
