//
//  UserDefaultsHelper.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import Foundation

class UserDefaultsHelper {
    static func isKeyPresentInUserDefaults(key: String) -> Bool {
        return UserDefaults.standard.object(forKey: key) != nil
    }
    
    // TODO: DRY
    static func nukeUserPaletteFromDefaults() {
        let defaults = UserDefaults.standard
        defaults.removeObject(forKey: "userPalettes")
        print("[--UserPaletteViewModel user defaults cleared for 'userPalettes' key.")
    }
}

extension Array: RawRepresentable where Element: Codable {
    public init?(rawValue: String) {
        guard let data = rawValue.data(using: .utf8),
              let result = try? JSONDecoder().decode([Element].self, from: data)
        else {
            return nil
        }
        self = result
    }

    public var rawValue: String {
        guard let data = try? JSONEncoder().encode(self),
              let result = String(data: data, encoding: .utf8)
        else {
            return "[]"
        }
        return result
    }
}
