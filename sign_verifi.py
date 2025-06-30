from ecdsa import SigningKey, VerifyingKey, NIST384p, BadSignatureError

# BƯỚC 1: Ông già Noel tạo cặp khóa riêng & công khai
print("🎅 Tạo cặp khóa...")
private_key = SigningKey.generate(curve=NIST384p)         # Khóa bí mật
public_key = private_key.verifying_key                    # Khóa công khai

# Lưu khóa vào file để mô phỏng thật
with open("santa_private.pem", "wb") as f:
    f.write(private_key.to_pem())

with open("santa_public.pem", "wb") as f:
    f.write(public_key.to_pem())

print("🔐 Khóa đã được lưu vào file.")

# BƯỚC 2: Ông già Noel viết thư & ký tên
message = "Merry Christmas, Alice! 🎁🎄".encode('utf-8')
signature = private_key.sign(message)

# Lưu chữ ký vào file
with open("letter_signature.sig", "wb") as f:
    f.write(signature)

print("\n📨 Ông già Noel đã ký lá thư và gửi đi.")

# BƯỚC 3: Bé Alice nhận thư và kiểm tra chữ ký
print("\n🧸 Bé Alice đang xác minh chữ ký...")

# Đọc lại khóa công khai và chữ ký từ file
with open("santa_public.pem", "rb") as f:
    alice_public_key = VerifyingKey.from_pem(f.read())

with open("letter_signature.sig", "rb") as f:
    received_signature = f.read()

# Thông điệp mà bé Alice nhận được(Giả mạo)
message = "Give me all presents, now! 🎁🎄".encode('utf-8')

# Bé Alice kiểm tra chữ ký
try:
    if alice_public_key.verify(received_signature, message):
        print("✅ Lá thư là thật! Chính ông già Noel đã ký.")
except BadSignatureError:
    print("❌ Chữ ký không hợp lệ! Có thể bố mẹ giả mạo 😅")

