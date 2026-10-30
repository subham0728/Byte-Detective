let active=1, solved=new Set();
const $=id=>document.getElementById(id);
const totalCases=()=>document.querySelectorAll('.case-link').length || 1;
function updateProgress(){
 const total=totalCases();
 $('star-count').textContent=solved.size;
 $('progress-bar').style.width=(solved.size/total*100)+'%';
 $('progress-text').textContent=`${solved.size} of ${total} cases solved`;
}
async function loadCase(id){
 active=id;
 const r=await fetch(`/api/case/${id}`), c=await r.json();
 document.querySelectorAll('.case-link').forEach(b=>b.classList.toggle('selected',+b.dataset.case===id));
 $('case-title').textContent=c.title;$('case-level').textContent=`⭐ ${c.level} CASE`;$('case-emoji').textContent=c.emoji;
 $('story').textContent=c.story;$('scene').src=`/static/images/${c.scene}`;
 $('clues').innerHTML=c.clues.map(x=>`<div class="clue">${x}</div>`).join('');
 $('code').value=c.broken;$('hint').hidden=true;$('success').hidden=true;$('result').innerHTML="<span>🤖</span><p>I'm ready! Fix the code and press <b>Check My Code</b>.</p>";
 $('run-btn').disabled=solved.has(id);$('run-btn').textContent=solved.has(id)?'CASE SOLVED ✓':'▶ CHECK MY CODE!';
 $('line-nums').innerHTML=c.broken.split('\n').map((_,i)=>i+1).join('<br>');
}
document.querySelectorAll('.case-link').forEach(b=>b.onclick=()=>loadCase(+b.dataset.case));
$('start-btn').onclick=()=>{$('welcome').hidden=true;$('how').hidden=true;$('game').hidden=false;loadCase(1);window.scrollTo({top:0,behavior:'smooth'})};
$('code').addEventListener('input',()=>{$('line-nums').innerHTML=$('code').value.split('\n').map((_,i)=>i+1).join('<br>')});
$('code').addEventListener('keydown',e=>{if(e.key==='Tab'){e.preventDefault();let s=e.target.selectionStart;e.target.setRangeText('    ',s,e.target.selectionEnd,'end')}});
$('hint-btn').onclick=async()=>{let r=await fetch(`/api/hint/${active}`),d=await r.json();$('hint').textContent='💡 HINT: '+d.hint;$('hint').hidden=false};
$('run-btn').onclick=async()=>{
 const btn=$('run-btn');btn.disabled=true;btn.textContent='CHECKING...';
 try{
  let r=await fetch('/api/check',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({case_id:active,code:$('code').value})}),d=await r.json();
  if(d.success){
   solved.add(active);$('star-count').textContent=solved.size;$(`done-${active}`).textContent='⭐';
   updateProgress();
   $('result').innerHTML=`<span>🎉</span><p><b>Awesome work!</b> Your code works!<br><code>${d.output.replaceAll('\n',' · ')}</code></p>`;
   $('suspect').textContent=d.suspect;$('explain').textContent=d.explain;$('success').hidden=false;
  }else{$('result').innerHTML='<span>🧐</span><p><b>Good try!</b> '+d.message+' Check the clues or ask for a hint.</p>'}
 }catch(e){$('result').innerHTML='<span>📡</span><p>Cannot reach the game server. Please restart app.py.</p>'}
 btn.disabled=solved.has(active);if(!solved.has(active))btn.textContent='▶ CHECK MY CODE!';
};
$('next-btn').onclick=()=>{const total=totalCases();let next=Array.from({length:total},(_,i)=>i+1).find(i=>!solved.has(i));if(next)loadCase(next);else{solved.clear();document.querySelectorAll('.case-link i').forEach(x=>x.textContent='○');$('star-count').textContent='0';updateProgress();loadCase(1)}};
