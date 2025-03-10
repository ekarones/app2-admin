const modalCreate = document.getElementById("modal-create");
const openModalCreate = document.getElementById("open-modal-create");
const closeModalCreate = document.getElementById("close-modal-create");

const modalUpdate = document.getElementById("modal-update");
const modalUpdateButtons = document.getElementsByClassName("update-btn");
const openModalUpdate = document.getElementById("open-modal-update");
const closeModalUpdate = document.getElementById("close-modal-update");

openModalCreate.addEventListener("click", () => {
  modalCreate.style.display = "flex";
});

closeModalCreate.addEventListener("click", () => {
  modalCreate.style.display = "none";
});

Array.from(modalUpdateButtons).forEach((button) => {
  button.addEventListener("click", function (event) {
    const id = this.getAttribute("data-id");
    const name = this.getAttribute("data-title");
    const description = this.getAttribute("data-description");

    modalUpdate.style.display = "flex";

    modalUpdate.querySelector("#id-notification").textContent = id;
    modalUpdate.querySelector("#title").value = name;
    modalUpdate.querySelector("#description").value = description;
    modalUpdate
      .querySelector("#updateForm")
      .setAttribute("action", "update_notification/" + id);
  });
});

closeModalUpdate.addEventListener("click", () => {
  modalUpdate.style.display = "none";
});
