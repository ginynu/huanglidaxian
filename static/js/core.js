var bgs = document.querySelectorAll('.bgs')
for(var i=0;i<bgs.length;i++) {
bgs[i].idx = i;
bgs[i].onclick = function() {
bgs[this.idx].setAttribute('class', 'bgs hide');
bgs[(this.idx+1)%2].setAttribute('class', 'bgs');
}
}