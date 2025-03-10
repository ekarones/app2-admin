const modalCreate = document.getElementById("modal-create");
const openModalCreate = document.getElementById("open-modal-create");
const closeModalCreate = document.getElementById("close-modal-create");

const modalUpdate = document.getElementById("modal-update");
const modalUpdateButtons = document.getElementsByClassName("update-btn");
const openModalUpdate = document.getElementById("open-modal-update");
const closeModalUpdate = document.getElementById("close-modal-update");

const modalImage = document.getElementById("modal-image");
const modalImageButtons = document.getElementsByClassName("show-image-btn");
const openModalImage = document.getElementById("open-modal-image");
const closeModalImage = document.getElementById("close-modal-image");
const RefImage = document.getElementById("ref-image");

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

    modalUpdate.querySelector("#id-disease").textContent = id;
    modalUpdate.querySelector("#name").value = name;
    modalUpdate.querySelector("#description").value = description;
    modalUpdate
      .querySelector("#updateForm")
      .setAttribute("action", "update_disease/" + id);
  });
});

closeModalUpdate.addEventListener("click", () => {
  modalUpdate.style.display = "none";
});

Array.from(modalImageButtons).forEach((button) => {
  button.addEventListener("click", function (event) {
    const api_url = this.getAttribute("data-api-url");
    const img_name = this.getAttribute("data-image-name");
    const image_url = `${api_url}?filename=${img_name}`;

    RefImage.src = image_url;
    modalImage.style.display = "flex";
  });
});
closeModalImage.addEventListener("click", () => {
  modalImage.style.display = "none";
});
