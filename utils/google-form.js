/*global FormApp, Logger, SpreadsheetApp*/
var Form = function (param) {
    this.form = FormApp.create(param.name);
    this.phrases = [];
    this.form.setTitle(param.title);
    Logger.log('Published URL:\n' + this.form.getPublishedUrl());
    Logger.log('Editor URL:\n' + this.form.getEditUrl());
};

Form.prototype.setInstruction = function (message) {

    var item = this.form.addSectionHeaderItem();

    item.setTitle('Istruzioni ')
        .setHelpText(message);
    // this.form.addPageBreakItem();
};

Form.prototype.readSpreadsheet = function (spreadsheetID) {

    var sheet = SpreadsheetApp.openById(spreadsheetID);
    // TODO - uncomment the getRange parameter to get all rows
    var rows = sheet.getRange('A2:I129').getValues();
    var premise1,
        premise2,
        conclusion,
        TW,
        phrase,
        self = this;

    rows.forEach(function (row) {
        TW = row[8].toLowerCase();
        premise1 = row[5].replace('...', TW);
        premise2 = row[6].replace('...', TW);
        conclusion = row[7];
        phrase = '\nP1: ' + premise1 + '\n\n';
        phrase += 'P2: ' + premise2 + '\n\n------------------------------\n\n';
        phrase += conclusion + '\n';
        self.phrases.push(phrase);
    });
};

Form.prototype.setUserQuestions = function () {

    var item;

    item = this.form.addTextItem();
    item.setTitle('Nickname').setRequired(true);;
    item = this.form.addTextItem();
    item.setTitle('Età').setRequired(true);;
    item = this.form.addMultipleChoiceItem();
    item.setTitle('Genere (M/F)')
        .setChoices([
            item.createChoice('M'),
            item.createChoice('F')
        ])
        .setRequired(true);;
    // this.form.addPageBreakItem();
};

Form.prototype.setQuestions = function () {

    var item,
        form = this.form;

    this.phrases.forEach(function (phrase, index) {
        form.addSectionHeaderItem()
            .setTitle('Domanda ' + (index + 1))
            .setHelpText(phrase);
        item = form.addMultipleChoiceItem();
        item.setTitle('La conclusione segue le premesse?')
            .setChoices([
                item.createChoice('Si'),
                item.createChoice('No')
            ])
            .setRequired(true);
        // form.addPageBreakItem();
    });
};

Form.prototype.setConclusion = function (message) {

    this.form.addSectionHeaderItem()
        .setTitle(message.title)
        .setHelpText(message.subTitle);
};

Form.prototype.addPageBreakItem = function () {

    this.form.addPageBreakItem();
};

function main(){
    /*
     * This script creates a quiz form in google from an existing spreadsheet.
     * To launch the script: "Run -> main"
     * To see the log of this script: "View -> Logs"
     */
    var form = new Form({
        title: 'Linguaggio e argomentazione',
        name: 'form-online'
    });

    var instruction;

    instruction = 'State per iniziare un esperimento che riguarda il rapporto tra linguaggio e argomentazione.\nTrovate di seguito le istruzioni. I risultati saranno anonimi.\n\n';
    form.setInstruction(instruction);
    form.addPageBreakItem();
    form.setUserQuestions();
    instruction = 'Leggerete degli argomenti composti da tre frasi:\n\n';
    instruction += 'due premesse (P1 e P2) e una conclusione (C).\n\n';
    instruction += 'Dopo aver letto attentamente le tre frasi, giudicate se la conclusione segue dalle premesse, rispondendo:\n\n';
    instruction += 'SI (La conclusione SEGUE dalle premesse)\n\n';
    instruction += 'oppure:\n\n';
    instruction += 'NO (La conclusione NON SEGUE dalle premesse)';
    form.setInstruction(instruction);
    // The spreadsheet id corresponds to the spreadsheet file named arguments-online.
    form.readSpreadsheet('1e3UnVn82xXnbDd5RjAEtfvx8YjLYsJDLpCs3OJJaGGY');
    form.setQuestions();
    form.setConclusion({
        title: 'Grazie per la vostra partecipazione all\'esperimento!',
        subTitle: '\nCliccate su "Submit" per salvare le risposte.\n\nDopo aver clicccato su "Submit", i risultati del test potranno essere visualizzati e modificati fino al 15 settembre 2015.'
    });
}
