//
//  ColourMapping.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-16.
//

import Foundation
import UIKit

final class ColourMapper: ObservableObject {

    // Data
    private(set) var colourMap: [VColour] = []
    
    // Singleton instance
    static let shared = ColourMapper()
    
    // Prevents external instantiation
    private init() {
        print("ColourMapper init called")
        self.createColourMapFromCSV { cM in
            self.colourMap = cM
        }
    }
    
    func createColourMapFromCSV(completion: @escaping ([VColour]) -> Void) {
        print("creating colourMap from CSV.")
        // Check if colourMap is already populated
        if !colourMap.isEmpty {
            completion(colourMap) // Return existing colourMap if already populated
            return
        }
        
        // Proceed to read the CSV and populate colourMap
        var coloursFromCSV: [VColour] = []
        
        guard let filePath = Bundle.main.path(forResource: "colourmap", ofType: "csv") else {
            print("CSV FILE NON-EXISTENT.")
            completion(coloursFromCSV)
            return
        }
        
        DispatchQueue.global(qos: .background).async {
            do {
                let csvData = try String(contentsOfFile: filePath, encoding: .utf8)
                let rows = csvData.components(separatedBy: "\n")
                let rowsWithoutHeaders = rows.dropFirst()
                
                for row in rowsWithoutHeaders {
                    let columns = row.components(separatedBy: ",")
                    
                    if columns.count == 2 {
                        let colourName = columns[0]
                        let hexCode = columns[1]
                        
                        let rgbCode: RGBTuple = ColourHelper.hexToRGB(hex: hexCode)
                        let uiColour: UIColor = UIColor(hex: hexCode)
                        let colour = VColour(name: colourName, hexCode: hexCode, rgbCode: rgbCode, uiColour: uiColour)
                        coloursFromCSV.append(colour)
                    }
                }
                DispatchQueue.main.async {
                    self.colourMap = coloursFromCSV // Store the fetched colours
                    completion(coloursFromCSV)
                }
            } catch {
                print("Error reading CSV file: \(error)")
                DispatchQueue.main.async {
                    completion(coloursFromCSV) // Return empty array on error
                }
            }
        }
    }
}
