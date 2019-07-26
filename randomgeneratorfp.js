function getRandomGen(){
  var list =['character1.html', 'character3.html', 'character5.html', 'character6.html', 'character4first.html'];
  var listLen = list.length;
  var num = Math.floor(Math.random() * listLen);
  var word = list[num];
  document.getElementById("experience").innerHTML = word;
  window.open(word);
  link= document.getElementsById("linkme");
}
