package javamaildemo;
import java.util.*;  
import javax.mail.*;  
import javax.mail.internet.*;  
/**
 * This class is used to send simple email.
 * @author codesjava
 */
public class SendSimpleEmail { 
 final String senderEmailId = "huuthuy2000@gmail.com";
 final String senderPassword = "tranhuuthuy";
 final String emailSMTPserver = "smtpout.secureserver.net";
 
public SendSimpleEmail(String receiverEmail, 
		String subject, String messageText) {	
 
	Properties props = new Properties();
	props.put("mail.smtp.auth", "true");
	props.put("mail.smtp.host", emailSMTPserver);
 
	try { 			
		Authenticator auth = new SMTPAuthenticator();
                Session session = Session.getInstance(props, auth);
		Message message = new MimeMessage(session);
		message.setFrom(new InternetAddress(senderEmailId));
		message.setRecipients(Message.RecipientType.TO, 
				InternetAddress.parse(receiverEmail));
		message.setSubject(subject);
		message.setText(messageText);
 
		Transport.send(message); 
		System.out.println("Email send successfully."); 
    } catch (Exception e) {
	e.printStackTrace();
    System.err.println("Error in sending email.");
   }
}
 
private class SMTPAuthenticator extends 
  javax.mail.Authenticator {
    public PasswordAuthentication 
       getPasswordAuthentication() {
        return new PasswordAuthentication(senderEmailId, 
        		senderPassword);
    }
}
 
public static void main(String[] args) {
	new SendSimpleEmail("huuthuy2000@gmail.com", 
	     "Test Email", "Hi,\n\n This is a test email.");
    }
}
