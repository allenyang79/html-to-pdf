// html2pdf.js
var page = new WebPage();
var system = require("system");
// change the paper size to letter, add some borders
// add a footer callback showing page numbers
 
//console.dir(system.args);
//phantom.exit();

page.paperSize = {
  format: "Letter",
  orientation: "portrait",
  margin: {left:"2.5cm", right:"2.5cm", top:"1cm", bottom:"1cm"},
  footer: {
    height: "0.9cm",
    contents: phantom.callback(function(pageNum, numPages) {
      return "<div style='text-align:center;'><small> page:" + pageNum +
        " / " + numPages + "</small></div> ";
    })
  }
};
page.zoomFactor = 1;
// assume the file is local, so we don't handle status errors
/*
page.open(system.args[1], function (status) {
  // export to target (can be PNG, JPG or PDF!)
  page.render(system.args[2]);
  phantom.exit();
});
*/
var html = system.args[1];
if(!html){
    console.error("args is incorrent");
    phantom.exit();
}

page.setContent(html,"tmp.html");




/*
nowStr = (parseInt((+new Date())*0.001));
file = "static/test"+nowStr+".pdf";
page.render(file,{format:"pdf"});
console.log(file);
phantom.exit();
*/

/*
console.log(system.args[0]);
console.log(system.args[1]);
console.log(system.args[2]);
*/
if(system.args[2]){
    console.log(system.args[2]);
    page.render(system.args[2],{format:"pdf"});
    phantom.exit();
}else{
    page.render("/dev/stdout",{format:"pdf"})
    phantom.exit();
}

