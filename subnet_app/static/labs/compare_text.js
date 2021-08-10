document.getElementById("go_button").addEventListener("click", function(){

    var correct = document.getElementById("correct").innerHTML;
    var user_answer = document.getElementById("user_input").value;
    var user_answer_text_input = document.getElementById("user_input")
    var input_instructions = document.getElementById("input_instructions")

    if (user_answer == correct){
       var correct_answer_textarea = document.getElementById("correct_answer_textarea");
       correct_answer_textarea.classList.remove("hidden");
       user_answer_text_input.classList.remove("error");
       user_answer_text_input.classList.add("correct");
       input_instructions.classList.add("hidden");
    } else {
       user_answer_text_input.classList.add("error");
    }
});

// START WHATS THE MASK CHECKING

document.getElementById("go_button_howmanybits").addEventListener("click", function(){

    var correct_howmanybits = document.getElementById("correct_howmanybits").innerHTML;
    var user_answer_howmanybits = document.getElementById("user_input_howmanybits").value;
    var user_answer_text_input = document.getElementById("user_input_howmanybits")
//    var input_instructions = document.getElementById("input_instructions")

    if (user_answer_howmanybits == correct_howmanybits){
       var howmanybits_correct_answer_area = document.getElementById("howmanybits_correct_answer_area");
       howmanybits_correct_answer_area.classList.remove("hidden");
       user_answer_text_input.classList.remove("error");
       user_answer_text_input.classList.add("correct");
//       input_instructions.classList.add("hidden");
    } else {
       user_answer_text_input.classList.add("error");
    }
});

// START HOW MANY BITS CHECKING CODE

document.getElementById("go_button_hosts_and_networks").addEventListener("click", function(){

    var correct_count_of_hosts = document.getElementById("correct_hosts").innerHTML;
    var correct_number_of_subnets = document.getElementById("correct_subnets").innerHTML;

    var user_answer_count_of_hosts = document.getElementById("user_input_hosts").value;
    var user_answer_text_input_hosts = document.getElementById("user_input_hosts")

    var user_answer_count_of_subnets = document.getElementById("user_input_networks").value;
    var user_answer_text_input_subnets = document.getElementById("user_input_networks")
//    var input_instructions = document.getElementById("input_instructions")

    if (user_answer_count_of_hosts == correct_count_of_hosts && user_answer_count_of_subnets == correct_number_of_subnets){
       var howmany_correct_answer_area = document.getElementById("howmany_correct_answer_area");
       howmany_correct_answer_area.classList.remove("hidden");
       user_answer_text_input_hosts.classList.remove("error");
       user_answer_text_input_subnets.classList.remove("error");
       user_answer_text_input_hosts.classList.add("correct");
       user_answer_text_input_subnets.classList.add("correct");
//       input_instructions.classList.add("hidden");
    } else {
       user_answer_text_input_hosts.classList.add("error");
        user_answer_text_input_subnets.classList.add("error");
    }
});
