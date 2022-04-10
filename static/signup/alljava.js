function setuptebs(){
    document.querySelectorAll(".tabs__btn").forEach(button =>{
      button.addEventListener("click", () => {
        const tabn = button.dataset.toggle;
        const elem = button.parentElement;
        if (tabn=="user"){

          var e=document.getElementById("journalistb")
         e.classList.remove("active")
          var e=document.getElementById("userb")
         e.classList.add("active")

          var z=document.getElementById("user")
          z.classList.add("active")
          var z=document.getElementById("journalist")
          z.classList.remove("active")
        }
       else if(tabn == "journalist"){
         
         var e=document.getElementById("userb")
         e.classList.remove("active")
         var e=document.getElementById("journalistb")
         e.classList.add("active")
  
         var z=document.getElementById("user")
         z.classList.remove("active")
         var z=document.getElementById("journalist")
         z.classList.add("active")
       }
      }) 
    });
  }
  document.addEventListener("DOMContentLoaded", () => {
    setuptebs();
  })