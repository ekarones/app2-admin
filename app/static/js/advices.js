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
    const name = this.getAttribute("data-name");
    const description = this.getAttribute("data-description");

    modalUpdate.style.display = "flex";

    modalUpdate.querySelector("#id-advice").textContent = id;
    modalUpdate.querySelector("#disease_name").value = name;
    modalUpdate.querySelector("#description").value = description;
    modalUpdate
      .querySelector("#updateForm")
      .setAttribute("action", "update_advice/" + id);
  });
});

closeModalUpdate.addEventListener("click", () => {
  modalUpdate.style.display = "none";
});

// Cerrar modal al hacer clic fuera del contenido
// window.addEventListener("click", (event) => {
//     if (event.target === modal) {
//         modal.style.display = "none";
//     }
// });
