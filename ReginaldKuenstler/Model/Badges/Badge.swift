//
//  Badge.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import Foundation

struct Badge {
    let name: String
    let imageName: String
    let information: String
    let distance: Double
    
    init?(from dictionary: [String: String]) {
        guard
            let name = dictionary["name"],
            let imageName = dictionary["imageName"],
            let information = dictionary["information"],
            let distanceString = dictionary["distance"],
            let distance = Double(distanceString)
        else {
            return nil
        }
        self.name = name
        self.imageName = imageName
        self.information = information
        self.distance = distance
    }
    
    static let allBadges: [Badge] = {
        guard let fileURL = Bundle.main.url(forResource: "badges", withExtension: "txt") else {
            fatalError("No badges.txt file found")
        }
        do {
            let jsonData = try Data(contentsOf: fileURL, options: .mappedIfSafe)
            let jsonResult = try JSONSerialization.jsonObject(with: jsonData) as! [[String: String]]
            return jsonResult.compactMap(Badge.init)
        } catch {
            fatalError("Cannot decode badges.txt")
        }
    }()
    
    static func best(for distance: Double) -> Badge {
        return allBadges.filter { $0.distance < distance }.last ?? allBadges.first!
    }
    
    static func next(for distance: Double) -> Badge {
        return allBadges.filter { distance < $0.distance }.first ?? allBadges.last!
    }
}

// MARK: - Equatable

extension Badge: Equatable {
    static func ==(lhs: Badge, rhs: Badge) -> Bool {
        return lhs.name == rhs.name
    }
}
