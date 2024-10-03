from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# BCD 변환 함수
def decimal_to_bcd(decimal):
    bcd = ''
    for digit in str(decimal):
        bcd += f'{int(digit):04b} '  # 각 자리 숫자를 4비트로 변환하고 공백으로 구분
    return bcd.strip()

# BIN 변환 함수
def decimal_to_bin(decimal):
    return f'{decimal:b}'  # 이진수로 변환

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_question():
    decimal_number = random.randint(0, 999)
    convert_type = random.choice(['BIN', 'BCD'])

    # 정답 계산
    if convert_type == 'BIN':
        correct_answer = decimal_to_bin(decimal_number)
    else:
        correct_answer = decimal_to_bcd(decimal_number)

    return jsonify({
        'decimal_number': decimal_number,
        'convert_type': convert_type,
        'correct_answer': correct_answer
    })

if __name__ == '__main__':
    app.run(debug=True)
