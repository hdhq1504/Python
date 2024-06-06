import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP

class RSASignatureApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RSA Signature App")

        # Generate RSA key pair
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

        # Create UI elements
        self.create_ui()

    def create_ui(self):
        # Key generation section
        key_label = tk.Label(self.root, text="RSA Key Generation")
        key_label.pack()

        private_key_label = tk.Label(self.root, text="Private Key:")
        private_key_label.pack()
        private_key_text = tk.Text(self.root, height=5, width=50)
        private_key_text.insert(tk.END, self.private_key.decode())
        private_key_text.pack()

        public_key_label = tk.Label(self.root, text="Public Key:")
        public_key_label.pack()
        public_key_text = tk.Text(self.root, height=5, width=50)
        public_key_text.insert(tk.END, self.public_key.decode())
        public_key_text.pack()

        # Message signing section
        sign_label = tk.Label(self.root, text="Message Signing")
        sign_label.pack()

        message_label = tk.Label(self.root, text="Enter Message:")
        message_label.pack()
        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack()

        sign_button = tk.Button(self.root, text="Sign Message", command=self.sign_message)
        sign_button.pack()

        signature_label = tk.Label(self.root, text="Signature:")
        signature_label.pack()
        self.signature_text = tk.Text(self.root, height=5, width=50)
        self.signature_text.pack()

        # Message verification section
        verify_label = tk.Label(self.root, text="Message Verification")
        verify_label.pack()

        received_message_label = tk.Label(self.root, text="Received Message:")
        received_message_label.pack()
        self.received_message_entry = tk.Entry(self.root)
        self.received_message_entry.pack()

        received_signature_label = tk.Label(self.root, text="Received Signature:")
        received_signature_label.pack()
        self.received_signature_entry = tk.Entry(self.root)
        self.received_signature_entry.pack()

        verify_button = tk.Button(self.root, text="Verify Signature", command=self.verify_signature)
        verify_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def sign_message(self):
        message = self.message_entry.get().strip()
        if not message:
            self.result_label.config(text="Please provide a message to sign.")
            return
        message = message.encode()
        h = SHA256.new(message)
        signer = pkcs1_15.new(self.key)
        signature = signer.sign(h)
        self.signature_text.delete(1.0, tk.END)
        self.signature_text.insert(tk.END, signature.hex())

        # Encrypt the message with the recipient's public key
        recipient_key = RSA.import_key(self.public_key)
        cipher = PKCS1_OAEP.new(recipient_key)
        encrypted_message = cipher.encrypt(message)
        self.received_message_entry.delete(0, tk.END)
        self.received_message_entry.insert(0, encrypted_message.hex())

    def verify_signature(self):
        received_message = self.received_message_entry.get().strip()
        received_signature = self.received_signature_entry.get().strip()
        if not received_message:
            self.result_label.config(text="Please provide a received message.")
            return
        
        try:
            received_message = bytes.fromhex(received_message)
            if received_signature:
                received_signature = bytes.fromhex(received_signature)
            else:
                self.result_label.config(text="No received signature provided. Signature verification skipped.")
                return

            # Decrypt the received message with the recipient's private key
            cipher = PKCS1_OAEP.new(self.key)
            decrypted_message = cipher.decrypt(received_message)

            # Verify the signature
            h = SHA256.new(decrypted_message)
            verifier = pkcs1_15.new(self.key.publickey())
            verifier.verify(h, received_signature)
            self.result_label.config(text="Signature is valid. Decryption successful: {}".format(decrypted_message.decode()))
        except (ValueError, TypeError, KeyError, IndexError):
            self.result_label.config(text="Failed to decrypt received message or invalid signature.")
        except pkcs1_15.VerificationError:
            self.result_label.config(text="Received signature is invalid.")
        except Exception as e:
            self.result_label.config(text="Error: {}".format(str(e)))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RSASignatureApp()
    app.run()
