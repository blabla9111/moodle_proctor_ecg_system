describe("Add/Delete proctoring", () => {
  const EMAIL = "admin";
  const PASSWORD = "Dinara06052002@";
  const EMAIL_STUDENT = "Dinara";
  const PASSWORD_STUDENT = "Dinara06!";

  const BASEURL = Cypress.config().baseUrl;
  const URLMAIN = BASEURL + "/";
  const URLLOGIN = BASEURL + "/login/index.php";
  const URLEDITPROCTOR = "/proctor_ecg/proctor_ecg_proct_edit/";

  it("Checking Add/Delete proctoring: success", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + URLEDITPROCTOR);
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("section[id=region-main] > div").contains(
      "Запрос выполнен. Изменения сохранены."
    );
  });

  it("Checking Add/Delete proctoring: incorrect input", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + URLEDITPROCTOR);
    cy.get("input[id=id_course_name]").click().type("JNIHIU");
    cy.get("input[id=id_quiz_name]").click().type("KHGUYUYIT");
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("section[id=region-main] > div ").contains(
      "Ошибка записи в базу данных"
    );
  });

  it("Checking Add/Delete proctoring: NO permission to take results", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL_STUDENT, PASSWORD_STUDENT);
    cy.visit(BASEURL + URLEDITPROCTOR);
    cy.get("div > input[id=id_submitbutton]").should("not.exist");
  });
  it("Checking Add/Delete proctoring: NO permission to take results (without login)", () => {
    cy.visit(BASEURL + URLEDITPROCTOR);
    cy.get("div > input[id=id_submitbutton]").should("not.exist");
  });
});
