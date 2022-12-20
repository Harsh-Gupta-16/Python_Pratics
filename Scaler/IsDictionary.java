package Scaler;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class IsDictionary {
    public static void main(String[] args) {
        ArrayList<String> A = new ArrayList<>(Arrays.asList("zkv", "zbc", "qpmxuj", "loovaowuxwhmsncbxcoks", "ejuvpvaboygp", "txdknlyjyhfixjswnkkufnux", "qghumeaylnlfdxfirc", "scxggbwkfnqduxwfn", "ggxrpnrvystmwcysyycqpev", "ozvsrtkjpre", "o", "cxfxtlsgypsfadpooef", "keffmznimkkasvwsrenzk", "etlyhnkoaugzqrcddiutei", "eylfpbnpljvrvipyamyehwqnq", "jwayyzpvscmpsajlfvgubfa", "zrzbmnmgqoo"));
        String B = "viwcblqmjdxhuyfkonrpzagste";
        System.out.println(dic(A, B));
    }

    public static int dic(ArrayList<String> A, String B) {
        HashMap<Character, Integer> hm = new HashMap<>();
        for (int i = 0; i < B.length(); i++) {
            hm.put(B.charAt(i), i);
        }
        for (int i = 0; i < A.size() - 1; i++) {
            String first = A.get(i);
            String second = A.get(i+1);
            for (int j = 0; j < first.length(); j++) {
                if (j==second.length())
                    return 0;
                if (hm.get(first.charAt(j)) < hm.get(second.charAt(j)))
                    break;
                if (hm.get(first.charAt(j)) > hm.get(second.charAt(j)))
                    return 0;
            }
        }
        return 1;
    }
}
