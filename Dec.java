

public class Dec {
    public static void main(String[] args) {
        String name="java program";
        String arr[]=name.split(" ");
        String nw="";
        System.out.println(arr);
        for(String wrd :arr)
        {
            for(int i=wrd.length()-1;i>=0;i--)
            {
                nw+=wrd.charAt(i);
            }
            nw+=" ";
        }
        System.out.println(nw);


         
    }
}
