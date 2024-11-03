//
//  ObjectInstance+CountFrequency.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import Foundation

func countFrequencies<T: Hashable>(array: [T]) -> [T: Int] {
    var frequencyDict: [T: Int] = [:]
    array.forEach { item in
        frequencyDict[item, default: 0] += 1
    }
    return frequencyDict
}