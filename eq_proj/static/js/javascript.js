function show_answer(q_id) 
{
    
    alert("div_answer_"+q_id);

    //var element_id = 

    var question_div = document.getElementById("div_answer_"+q_id);

    if (question_div.style.display === "none") {
        question_div.style.display = "block";
      } else {
        question_div.style.display = "none";
      }

}