document.getElementById("go_button").addEventListener("click", function(){

    var correct = document.getElementById("correct").innerHTML;
    var user_answer = document.getElementById("user_input").value;
    var user_answer_text_input = document.getElementById("user_input")
    if (user_answer == correct){
       var correct_answer_textarea = document.getElementById("correct_answer_textarea");
       correct_answer_textarea.classList.remove("hidden");
       user_answer_text_input.classList.remove("error");
       user_answer_text_input.classList.add("correct");
    } else {
       user_answer_text_input.classList.add("error");
    }
});