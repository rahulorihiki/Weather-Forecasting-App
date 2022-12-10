from flask import Flask , render_template
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt


listdata = [1,2,3,4,5]
df = pd.DataFrame(listdata)
# print(df)
app = Flask(__name__)

x = [2,4,6,8,10]
y = [3,6,9,12,15]
plt.plot(x,y)
plt.xlabel('Multiples of two')
plt.ylabel('Multiples of three')
plt.show()


@app.route('/', methods=['POST', 'GET'])
def index():
  return render_template('index.html', df = df)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)