describe("Take results", () => {
  const EMAIL = "admin";
  const PASSWORD = "Dinara06052002@";
  const EMAIL_STUDENT = "Dinara";
  const PASSWORD_STUDENT = "Dinara06!";

  const BASEURL = Cypress.config().baseUrl;
  const URLMAIN = BASEURL + "/";
  const URLLOGIN = BASEURL + "/login/index.php";
  const URLTAKERESULTS = "/proctor_ecg/proctor_ecg_table_download/";

  it("Checking take results: success", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + URLTAKERESULTS);
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("select[id=downloadtype_download]").should("exist");
  });

  it("Checking take code: incorrect input", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL, PASSWORD);
    cy.visit(BASEURL + URLTAKERESULTS);
    cy.get("input[id=id_course_name]").click().type("JNIHIU");
    cy.get("input[id=id_quiz_name]").click().type("KHGUYUYIT");
    cy.get("div > input[id=id_submitbutton]").click();
    cy.get("section[id=region-main] > div ").contains(
      "Не удается найти данную запись в таблице course базы данных.Проверьте на корректность введенные значения"
    );
  });

  it("Checking take code: NO permission to take results", () => {
    cy.visit(URLLOGIN);
    cy.login(EMAIL_STUDENT, PASSWORD_STUDENT);
    cy.visit(BASEURL + URLTAKERESULTS);
    cy.get("div > input[id=id_submitbutton]").should("not.exist");
  });
  it("Checking take code: NO permission to take results (without login)", () => {
    cy.visit(BASEURL + URLTAKERESULTS);
    cy.get("div > input[id=id_submitbutton]").should("not.exist");
  });
});
