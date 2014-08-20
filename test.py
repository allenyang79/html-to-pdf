import re
import arrow
import sys,os
from flask import Flask,request,make_response,send_file
import subprocess
import tempfile
#print "hello"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pdf",methods=["POST","GET"])
def pdf():
    html = request.data
    nowStr = arrow.get().format("YYYYMMDDHHmmss")
    html = html.replace("<%nowStr%>",nowStr)
    
    (fd, filename) = tempfile.mkstemp(prefix="",suffix=".pdf")
    
    #return filename
    p = subprocess.Popen(["phantomjs", "html_to_pdf.js",html,filename],
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT
    )
    stdout, stderr = p.communicate()
    #return str(stdout)

    #return filename 
    fileStr = filename
    #fileStr = re.sub(r"(\r|\t|\n)", "", fileStr)
    #fileStr.replace("(\t|\n|\r)","")
    return send_file(open(fileStr), as_attachment=True, attachment_filename="go.pdf")
   
    print str(len(stdout))
    
    response = make_response(stdout)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename={}.pdf'.format(nowStr)
    return response

    #return stdout
    #print html
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)




#from ghost import Ghost
#ghost = Ghost()
#page, extra_resources = ghost.open("http://jeanphi.fr")
#assert page.http_status==200 and 'jeanphix' in ghost.content
