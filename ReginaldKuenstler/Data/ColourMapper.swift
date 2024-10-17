//
//  ColourMapping.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import UIKit

// Has a dict of colour string names and their rgb/hex values
final class ColourMapper {
    
    // extract `colourmap.csv` and make a dict out of it
    // dict = { "Cadmium Red": "#FF2210" }
    var colourMap: [VColour] = []
    func createColourMapFromCSV() -> [VColour] {
        var coloursFromCSV: [VColour] = []
        
        guard let filePath = Bundle.main.path(forResource: "colourmap", ofType: "csv") else {
            print("CSV FILE NON-EXISTENT.")
            return coloursFromCSV
        }
        
        // read from csv
        do {
            let csvData = try String(contentsOfFile: filePath, encoding: .utf8)
            let rows = csvData.components(separatedBy: "\n")
            let rowsWithoutHeaders = rows.dropFirst()
            
            for row in rowsWithoutHeaders {
                let columns = row.components(separatedBy: ",")
                
                if columns.count == 2 {
                    let colourName = columns[0]
                    let hexCode = columns[1]
                    
                    let rgbCode: RGBTuple = ColourConverter.hexToRGB(hex: hexCode)
                    let uiColour: UIColor = UIColor(hex: hexCode)
                    let colour = VColour(name: colourName, hexCode: hexCode, rgbCode: rgbCode, uiColour: uiColour)
                    coloursFromCSV.append(colour)
                }
            }
        } catch {
            print("Error reading CSV file: \(error)")
        }
        // print(coloursFromCSV)
        self.colourMap = coloursFromCSV
        return coloursFromCSV
    }
}
