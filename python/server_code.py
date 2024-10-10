def letter_in_data(data):
    letters = 'qwertuiopasdfghjklzcvbnm'
    for i in data:
        if i in letters:
            return True
    return False

def is_in_data(thing, data):
	for i in data:
		if [i[0], i[1]] == thing:
			return [True, i]
	return [False, 0]

import math

def calculator(expression):
  """
  This function runs a simple calculator that can handle basic arithmetic operations,
  as well as square root, sine, cosine, and tangent.
  """

  # Replace "sqrt" with "math.sqrt"
  expression = expression.replace("sqrt", "math.sqrt")

  # Replace "sin", "cos", "tan" with corresponding math functions
  expression = expression.replace("sin", "math.sin")
  expression = expression.replace("cos", "math.cos")
  expression = expression.replace("tan", "math.tan")
  expression = expression.replace("^", "**")
  expression = expression.replace("pi", "math.pi")
  expression = expression.replace("e", "math.e")
  expression = expression.replace("factorial","math.factorial")

  result = eval(expression)
  return result

import sympy as sp
import re

def extract_coefficients(equation):
  """Extracts the coefficients from a linear equation."""
  match = re.match(r"(-?\d*)x?\s*(\+|\-)?\s*(-?\d*)y\s*=\s*(-?\d*)", equation)
  if match:
    a = int(match.group(1)) if match.group(1) else 0
    b = int(match.group(3)) if match.group(2) == "+" else -int(match.group(3))
    c = int(match.group(4))
    return a, b, c
  else:
    raise ValueError("Please double check you equation, hase to be in ax+by=c form, even if a or b is 1 or 0")

def solve_linear_equations(eq1, eq2):
  """Solves a system of two linear equations using Cramer's Rule."""

  # Get the equations from the user

  # Extract the coefficients
  a, b, c = extract_coefficients(eq1)
  d, e, f = extract_coefficients(eq2)

  # Calculate determinants
  D = a * e - b * d
  Dx = c * e - b * f
  Dy = a * f - c * d

  # Check for a unique solution
  if D == 0:
    if Dx == 0 and Dy == 0:
      return "Infinite Solutions"
    else:
      return "No Solution"
  else:
    # Calculate and display the solution
    x = Dx / D
    y = Dy / D
    print("\nSolution:")
    print(f"x = {x}")
    print(f"y = {y}")
    return f"x = {x}  y = {y}"


import hashlib
def hashedinfo(username, password):
	content = username
	hash_object = hashlib.sha256(content.encode('utf-8'))
	hex_dig = hash_object.hexdigest()
	hash_object1 = hashlib.md5(hex_dig.encode('utf-8'))
	hex_dig1 = hash_object1.hexdigest()
	content1 = password
	hash_object2 = hashlib.sha256(content1.encode('utf-8'))
	hex_dig2 = hash_object2.hexdigest()
	hash_object3 = hashlib.md5(hex_dig2.encode('utf-8'))
	hex_dig3 = hash_object3.hexdigest()
	final = f"Hashed version of username: {hex_dig1}\nHashed version of password: {hex_dig3}"
	return [hex_dig1,hex_dig3]
def encode(thing):
    a = hashedinfo(thing[0],thing[1])
    a.append(thing[2])
    return a


import sys
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app)
#put hashing print over here
@app.route('/submit', methods=['POST'])

def submit_data():
    data = request.get_json()
    u_and_p = [data['name'], data['message']]
    try:
        a = data['url']
    except:
        a = 'idk'
    if a != "idk":
        try:
            if u_and_p == ['','']:
                return jsonify({"message": f"NO TROLLING ALLOWED, MUST ENTER SOMETHING!", "url":"pythonanywhere"}), 200
            u_and_p.append(data['url'])
            with open('idk.txt', 'a') as fin:
                fin.write(f"{u_and_p}\n") #ONLY FOR RECOVERY AND FOR ME TO CHECK FOR TROLLERS
            a = encode(u_and_p)
            with open('data.txt', 'a') as fin:
                fin.write(f"{a}\n")
            with open('data.txt', 'r') as fin:
                contents = fin.readlines()  # Read all lines
                single_line = ''.join(contents)  # Join lines into a single string
            return jsonify({"message": f"Stored!", "url":"pythonanywhere"}), 200
        except:
            return jsonify({"message": "ERROR", "url":"pythonanywhere"}), 200
    e1  = u_and_p[0]
    equation1 = e1
    e2 = u_and_p[1]
    equation2 = e2
    if "crash" in equation2:
        return jsonify({"message": "chrome://restart", "url":"pythonanywhere"}), 200
    j = 0
    c = hashedinfo(u_and_p[0], u_and_p[1])
    response = {"message": "some data"}
    if False:
      print('How did you get here?')
    else:
        try:
            if equation1 != "" and equation2 == "":
               return jsonify({"message": str(calculator(equation1)), "url":"pythonanywhere"}), 200
            elif equation1 == "" and equation2 !="":
                return jsonify({"message": str(calculator(equation2)), "url":"pythonanywhere"}), 200
            elif equation1 != "" and equation2 !=""and (letter_in_data(equation1)==False and letter_in_data(equation2)==False):
                import function as f
                try:
                    f.check_for_valid_equation(str(equation1), str(equation2))
                except:
                    return jsonify({"message": str(solve_linear_equations(str(equation1), str(equation2))), "url":"pythonanywhere"}), 200
            else:
                return jsonify({"message": "Error: Please make sure no letters are present except x or y", "url":"pythonanywhere"}), 200
        except Exception as e:
            print("Received")
            err_message = str(e)
            if "division by zero" in err_message:
                return jsonify({"message": "Error: Attempted Division by 0"}), 200
            elif "equation format" in err_message:
                if e1=="" or e2 == "":
                    return jsonify({"message": "Error: Please Check your expression, make sure there is no variables"}), 200
                return jsonify({"message": "Error: 2-variable equations must be entered in ax+by=c form"}), 200
            elif "not defined" in err_message:
                return jsonify({"message": "Error: Please use valid variables (x and y) in the equations."}), 200
            else:
                return jsonify({"message": f"Error evaluating expression: {err_message}"}), 100

#quads















@app.route('/quad', methods=['POST'])
def s():
    data = request.get_json()
    import function as f
    try:
        return jsonify({'message':f"{f.calc_quad1(data['name'],data['message'])}"}), 200
    except Exception as e:
        return jsonify({'message':f'{e}'})
@app.route('/quad1', methods=['POST'])
def smth_l():
    data = request.get_json()
    import function as f
    try:
        return jsonify({'message':f"{f.solve_linear_quad(data['name'],data['message'])}"}), 200
    except Exception as e:
        return jsonify({'message':f'{e}'})

@app.route('/get/quad-info', methods=['POST'])
def smth_2():
    data = request.get_json()
    import function as f
    try:
        return jsonify({'message':f"{f.get_info(data['name'])}"}), 200
    except Exception as e:
        return jsonify({'message':f'{e}'})

@app.route('/grpah', methods = ['POST'])
def grapg():
    data = request.get_json()
    return jsonify({'message':'work in progress rn'}), 200



@app.route('/debug', methods=['POST'])
def se_data():
    data = request.get_json()
    if hashedinfo(data['password'], '') == ['7876fc69e05633dc67b328f0282c02c2', 'fa1269ea0d8c8723b5734305e48f7d46']:
        import code as c
        return jsonify({"message": f'Source code: {c.code()}'}), 200
    return jsonify({'message':'unauthorized'}), 200





# # This block is for running your Flask app
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
