import face_recognition
import qrcode
from employees import employees
from cryptography.fernet import Fernet
from face_recognition import *



# image_of_obama = face_recognition.load_image_file("images/barackobama.jpg")
# obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]
# image_of_unknown = face_recognition.load_image_file("images\ows_d64b80f9-8184-485e-b4f8-de5e46113da8.jpg")
# unknown_face_encoding = face_recognition.face_encodings(image_of_unknown)[0]
#
# result = face_recognition.compare_faces([obama_face_encoding], unknown_face_encoding, 0.5)
# if result[0]:
#     print("It's barack obama")
# else:
#     print("Unknown")
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

employees1 = employees(109019, "Ahad", 'Siddiqui', 1138, "03222135741")
qr.add_data(employees1.qr_code)
qr.add_data(employees1.e_first_name)
qr.add_data(employees1.e_last_name)
qr.add_data(employees1.e_id)
qr.add_data(employees1.e_contact)
qr.make(fit=True)
img = qr.make_image(fill = "#00A347", back_color = "white")
img.save("AhadSiddiqui.png")