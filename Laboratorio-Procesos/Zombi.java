import java.io.IOException;

public class Zombi {
    public static void main(String[] args) {
        try {
            System.out.println("[PADRE] Creando subproceso hijo (un simple comando ls)...");
            
            // Engendramos un proceso hijo en el Sistema Operativo
            Process hijo = new ProcessBuilder("ls").start();
            
            System.out.println("[PADRE] El hijo ha terminado su ejecucion.");
            System.out.println("[PADRE] ATENCION: El padre NO ejecutara wait() ni waitFor().");
            System.out.println("[PADRE] Entrando en bucle infinito. Revisa htop o ps para ver al ZOMBI...");
            
            // Bucle infinito para que el padre no muera y mantenga al zombi vivo
            while (true) {
                Thread.sleep(1000);
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
