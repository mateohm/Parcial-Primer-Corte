import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Leer desde entrada
        CharStream input = CharStreams.fromStream(System.in);

        ExpSeriesLexer lexer = new ExpSeriesLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        ExpSeriesParser parser = new ExpSeriesParser(tokens);

        ExpSeriesParser.ProgContext tree = parser.prog();

        double x = Double.parseDouble(tree.x.getText());
        int n = Integer.parseInt(tree.n.getText());

        double resultado = 0.0;
        for (int k = 0; k <= n; k++) {
            resultado += Math.pow(x, k) / factorial(k);
        }

        System.out.printf("Aproximación de e^%.2f con %d términos = %.10f\n", x, n, resultado);
    }

    private static long factorial(int k) {
        if (k <= 1) return 1;
        return k * factorial(k - 1);
    }
}
