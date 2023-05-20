// document.querySelector("#show-login").addEventListener("click",function(){
//     // document.querySelector(".popup.forms.login").classList.add("active");
//     // document.querySelector(".popup.forms.login").classLis
//     // document.querySelector(".main").classList.add("blur");
// });

// document.querySelector(".popup.forms.login .close-btn").addEventListener("click",function(){
//     document.querySelector(".popup.forms.login").classList.remove("active");
//     document.querySelector(".main").classList.remove("blur");

// });

// document.querySelector(".popup.forms.signup .close-btn").addEventListener("click",function(){
//     document.querySelector(".popup.forms.signup").classList.remove("active");
//     document.querySelector(".main").classList.remove("blur");

// });

const forms = document.querySelector(".forms"),
    pwShowHide = document.querySelectorAll(".hide-icon"),
    links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type = "text";
                eyeIcon.classList.replace("fa-eye-slash","fa-eye");
                return;
            } 
            password.type = "password";
            eyeIcon.classList.replace("fa-eye","fa-eye-slash");
        })
    })
})

// links.forEach(link => {
//     link.addEventListener("click", e => {
//         e.preventDefault();
//         forms.classList.toggle("show-signup");
//         let showSign = document.querySelector(".show-signup");
//         console.log(showSign);
//         if(showSign){
//             document.querySelector(".popup.forms.login").classList.add("not");
//             document.querySelector(".popup.forms.signup").classList.remove("not");
//         }
//         else{
//             document.querySelector(".popup.forms.signup").classList.add("not");
//             document.querySelector(".popup.forms.login").classList.remove("not");
//         }
//     })
// })