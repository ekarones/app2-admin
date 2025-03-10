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
    const username = this.getAttribute("data-username");
    const email = this.getAttribute("data-email");
    const password = this.getAttribute("data-password");

    modalUpdate.style.display = "flex";

    modalUpdate.querySelector("#id-admin").textContent = id;
    modalUpdate.querySelector("#username").value = username;
    modalUpdate.querySelector("#email").value = email;
    modalUpdate.querySelector("#password").value = password;
    modalUpdate
      .querySelector("#updateForm")
      .setAttribute("action", "update_admin/" + id);
  });
});

closeModalUpdate.addEventListener("click", () => {
  modalUpdate.style.display = "none";
});
