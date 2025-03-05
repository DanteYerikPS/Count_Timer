import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TempDigital {
    private static int seconds;
    private static JLabel timeLabel;
    private static Timer timer;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Temporizador Digital");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());

        timeLabel = new JLabel("00:00", SwingConstants.CENTER);
        timeLabel.setFont(new Font("Arial", Font.BOLD, 30));
        frame.add(timeLabel);

        JLabel inputLabel = new JLabel("Ingresa los segundos:");
        frame.add(inputLabel);

        JTextField inputField = new JTextField(5);
        frame.add(inputField);

        JButton startButton = new JButton("Iniciar Temporizador");
        frame.add(startButton);

        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    seconds = Integer.parseInt(inputField.getText());
                    startTimer();
                } catch (NumberFormatException ex) {
                    timeLabel.setText("Ingrese un número válido");
                }
            }
        });

        frame.setVisible(true);
    }

    private static void startTimer() {
        if (timer != null && timer.isRunning()) {
            timer.stop();
        }
        
        timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (seconds > 0) {
                    int mins = seconds / 60;
                    int secs = seconds % 60;
                    timeLabel.setText(String.format("%02d:%02d", mins, secs));
                    seconds--;
                } else {
                    timeLabel.setText("¡Tiempo finalizado!");
                    timer.stop();
                }
            }
        });
        timer.start();
    }
}
