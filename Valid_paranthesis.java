import java.util.*;
public class Valid_paranthesis {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        
        
        for(char ch :s.toCharArray())
        {
            if(ch =='(' || ch=='{' || ch=='[')
            {
                stk.push(ch);
            }
            else{
                char tp = stk.pop();
                if((ch==')' && tp!='(' )||(ch=='}' && tp!='{' )||(ch==']' && tp!='[' ))
                {
                    return false;
                }
                                
            }

        }


            return stk.isEmpty();

    
}
    public static void main(String[] args) {
        Valid_paranthesis obj = new Valid_paranthesis();

        System.out.println(obj.isValid("(){}[]"));  // true
        System.out.println(obj.isValid("(]"));      
        // System.out.println(obj.isValid("({[]})"));  
        // System.out.println(obj.isValid("((("));     
    }
}
