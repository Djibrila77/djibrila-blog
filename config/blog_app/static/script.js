

window.onbeforeunload = function () {
    window.scrollTo(0, 0);
};

function toggleText(btn) {
    
    const parent = btn.parentElement;
    const extrait = parent.querySelector('.extrait');
    const complet = parent.querySelector('.complet');

            if (complet.style.display === "none") {
                complet.style.display = "inline"; 
                extrait.style.display = "none";   
                btn.innerHTML = "Voir moins";    
            } else {
                complet.style.display = "none";
                extrait.style.display = "inline"; 
                btn.innerHTML = "Voir plus";      
            }
        }
                
        
    