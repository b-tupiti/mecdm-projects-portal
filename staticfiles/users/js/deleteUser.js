let deleteButtons = document.querySelectorAll(".delete-user");
let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

deleteButtons.forEach((deleteButton) => {
  deleteButton.addEventListener("click", async (e) => {
    // e.preventDefault()


    url = e.target["href"];


    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    });

    window.location.reload();
    response.json().then((data) => {
      console.log(data);
    });



  });
});
