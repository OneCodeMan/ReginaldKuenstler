//
//  MasterPaletteConstants.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import Foundation

struct MasterPaletteConstants {
    static let caravaggioImageStrings = ["caravaggio_portrait", "caravaggio0", "caravaggio1", "caravaggio2", "caravaggio3", "caravaggio4", "caravaggio5", "caravaggio6", "caravaggio7", "caravaggio8", "caravaggio9"]
    
    static let goyaImageStrings = ["goya_portrait", "goya0", "goya1", "goya2", "goya3", "goya4", "goya5", "goya6", "goya7"]
    
    static let vanGoghImageStrings = ["vangogh_portrait", "vangogh0", "vangogh1", "vangogh2", "vangogh3", "vangogh4", "vangogh5", "vangogh6", "vangogh7", "vangogh8", "vangogh9", "vangogh10", "vangogh11", "vangogh12"]
    
    static let munchImageStrings = ["munch_portrait", "munch0", "munch1", "munch2", "munch3", "munch4", "munch5", "munch6", "munch7"]
    
    static let botticeliImageStrings = ["boticelli_portrait", "boticcelli0", "boticcelli1", "boticcelli2", "boticcelli3", "boticcelli4", "boticcelli5", "boticcelli6", "boticcelli7"]
    
    static let gentileschiImageStrings = ["gentileschi_portrait", "gentileschi0", "gentileschi1", "gentileschi2", "gentileschi3", "gentileschi4", "gentileschi5", "gentileschi6"]
    
    static let picassoImageStrings = ["picasso_portrait", "picasso0", "picasso1", "picasso2", "picasso3", "picasso4", "picasso5", "picasso6", "picasso7"]
    
    static let sargentImageStrings = ["sargent_portrait", "sargent0", "sargent1", "sargent2", "sargent3", "sargent4", "sargent5", "sargent6", "sargent7"]
    
    static let siemiradzkiImageStrings = ["siemiradzki_portrait", "siemiradzki0", "siemiradzki1", "siemiradzki2", "siemiradzki3", "siemiradzki4", "siemiradzki5", "siemiradzki6", "siemiradzki7", "siemiradzki8"]
    
    static let hopperImageStrings = ["hopper_portrait", "hopper0", "hopper1", "hopper2", "hopper3", "hopper4", "hopper5", "hopper6", "hopper7", "hopper8", "hopper9", "hopper10", "hopper11", "hopper12", "hopper13"]
    static let johansenImageStrings = ["johansen_portrait", "johansen0", "johansen1", "johansen2", "johansen3", "johansen4", "johansen5"]
    
    static let masterPaletteImageStrings = [
        hopperImageStrings,
        siemiradzkiImageStrings,
        gentileschiImageStrings,
        goyaImageStrings,
        vanGoghImageStrings,
        
        johansenImageStrings,
        caravaggioImageStrings,
        munchImageStrings,
        botticeliImageStrings,
        picassoImageStrings,
        sargentImageStrings,
        
        // ... new down here
    ]
    
    // TODO: Add nationality
    static let masterPalettes: [MasterPalette] = [
        MasterPalette(imageStrings: vanGoghImageStrings, artistName: "Van Gogh"),
        MasterPalette(imageStrings: munchImageStrings, artistName: "Edvard Munch"),
        MasterPalette(imageStrings: hopperImageStrings, artistName: "Edward Hopper"),
        MasterPalette(imageStrings: goyaImageStrings, artistName: "Francisco Goya"),
        MasterPalette(imageStrings: caravaggioImageStrings, artistName: "Caravaggio"),
        MasterPalette(imageStrings: siemiradzkiImageStrings, artistName: "Henryk Siemiradzki"),
        MasterPalette(imageStrings: gentileschiImageStrings, artistName: "Artemisia Gentileschi"),
        MasterPalette(imageStrings: johansenImageStrings, artistName: "Viggo Johansen"),
        
        // TODO: these ones need assets.
        
        // MasterPalette(imageStrings: picassoImageStrings, artistName: "Pablo Picasso"),
        
        // MasterPalette(imageStrings: sargentImageStrings, artistName: "John Singer Sargent"),
    ]
    
}
