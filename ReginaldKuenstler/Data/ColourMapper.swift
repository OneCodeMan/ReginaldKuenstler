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
            
            for row in rows {
                let columns = row.components(separatedBy: ",")
                
                if columns.count == 2 {
                    let rgbCode = ColourConverter.hexToRGB(hex: columns[1])
                    let colour = VColour(name: columns[0], hexCode: columns[1], rgbCode: rgbCode)
                    coloursFromCSV.append(colour)
                }
            }
        } catch {
            print("Error reading CSV file: \(error)")
        }
        print(coloursFromCSV)
        self.colourMap = coloursFromCSV
        return coloursFromCSV
    }
}

struct VColour {
    var name: String = ""
    var hexCode: String = ""
    var rgbCode: RGBTuple = (r: 0, g: 0, b: 0)
}
