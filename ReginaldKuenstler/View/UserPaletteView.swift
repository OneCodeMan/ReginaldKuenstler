//
//  UserPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct UserPaletteView: View {
    @EnvironmentObject var userPaletteViewModel: UserPaletteViewModel
    
    // MARK: search logic
    @State var searchText: String = ""
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    // MARK: List edit mode
    @State private var isEditing: Bool = false
    @State private var isJiggling: Bool = false
    @State private var isPresentingConfirmation: Bool = false
    @State private var displayClearUserPaletteConfirmationAlert: Bool = false
    
    // MARK: Sheets and modals
    @State private var displayActionSheetInputTypes: Bool = false
    @State private var displayImageInputSheet: Bool = false
    @State private var displayCatalogSelectInputSheet: Bool = false
    
    // MARK: Selected item for deletion
    @State private var itemToDelete: (paletteColour: PaletteColour, groupName: String)?
    
    var body: some View {
        NavigationStack {
            VStack {
                Text("")
                    .toolbar {
                        if isEditing {
                            Button(String(localized: "Done")) {
                                withAnimation {
                                    isEditing.toggle()
                                    isJiggling.toggle()
                                }
                            }
                            .font(.defaultFontButton)
                        } else {
                            // TODO: Change to also include multi-select. Have an alert up
                            Button(String(localized: "Add")) {
                                displayActionSheetInputTypes = true
                            }
                            .font(.defaultFontButton)
//                            NavigationLink(destination: CreatePaletteWithPhotosView().environmentObject(userPaletteViewModel)) {
//                                Text(String(localized: "Add"))
//                                    .font(.defaultFontCaption)
//                            }
                        }
                    }
                
                // State 1: User has no palette colors and is not searching
                if userPaletteViewModel.userPaletteColours.isEmpty && searchText.isEmpty {
                    Text(String(localized: "You have no colours."))
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .multilineTextAlignment(.center)
                        .font(.defaultFontCaption)
                
                // State 2: User is searching but there are no results for the search term
                } else if !userPaletteViewModel.userPaletteColours.isEmpty && !searchText.isEmpty && userPaletteViewModel.filteredUserPaletteColours.isEmpty {
                    Text(String(localized: "No results found for \"\(searchText)\"."))
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .multilineTextAlignment(.center)
                        .font(.defaultFontCaption)
                
                // State 3: User is searching and there are results for the search term
                } else {
                    List {
                        ForEach(Array(userPaletteViewModel.groupedColours.keys).sorted(), id: \.self) { groupName in
                            if let groupItems = userPaletteViewModel.groupedColours[groupName], !groupItems.isEmpty {
                                VStack(alignment: .leading) {
                                    Text(groupName)
                                        .font(.defaultFontLargeTitle)
                                        .bold()
                                        .padding([.top, .leading], 8)
                                    
                                    LazyVGrid(columns: self.columns) {
                                        ForEach(groupItems) { cI in
                                            UserPaletteListItemView(paletteColourItem: cI)
                                                .jiggle(isEnabled: self.isJiggling)
                                                .onTapGesture {
                                                    withAnimation {
                                                        if isEditing {
                                                            self.isPresentingConfirmation = true
                                                            self.itemToDelete = (cI, groupName)
                                                        }
                                                    }
                                                }
                                                .contentShape(Rectangle())
                                                .onLongPressGesture(minimumDuration: 0.2) {
                                                    withAnimation {
                                                        isEditing = true
                                                        isJiggling = true
                                                        // delay(interval: 1.5) { self.isJiggling = false }
                                                    }
                                                }
                                                .overlay(
                                                    isEditing ? Button(action: {
                                                        self.isPresentingConfirmation = true
                                                        self.itemToDelete = (cI, groupName)
                                                    }) {
                                                        Image(systemName: "minus.circle.fill")
                                                            .foregroundColor(.red)
                                                    }
                                                    .padding(8) : nil,
                                                    alignment: .topTrailing
                                                )
                                        }
                                    }
                                    .listRowSeparator(.hidden)
                                    .padding()
                                }
                                .listRowSeparator(.hidden)
                            }
                        }
                    }
                }
            }
            .navigationTitle(String(localized: "Your Palette"))
            .font(.defaultFontLargeTitle)
            .toolbar {
                if isEditing {
                    // Add a toolbar item for the Clear All button
                    ToolbarItem(placement: .navigationBarLeading) {
                        Button(String(localized: "Clear All"), role: .destructive) {
                            displayClearUserPaletteConfirmationAlert = true
                        }
                        .font(.defaultFontCaption)
                    }
                }
                
            }
            .onAppear {
                print("USERPALETTEVIEW -- FETCHING USERPALETTES FROM USERPALETTEVIEWMODEL")
                self.userPaletteViewModel.fetchUserPalettes()
            }
            .alert(String(localized: "Are you sure you want to delete this colour?"), isPresented: $isPresentingConfirmation) {
                Button(String(localized: "Delete"), role: .destructive) {
                    withAnimation {
                        if let item = itemToDelete {
                            userPaletteViewModel.deletePaletteColourFromUserPalette(paletteColour: item.paletteColour, groupName: item.groupName)
                        }
                    }
                }
                Button(String(localized: "Cancel"), role: .cancel) { isPresentingConfirmation = false }
            }
            .actionSheet(isPresented: $displayActionSheetInputTypes) {
                ActionSheet(title: Text(String(localized: "Select Image")), 
                            message: Text(String(localized: "Please choose an option to select a photo")),
                            buttons: [
                                .default(Text(String(localized: "Image Input"))) {
                                    displayImageInputSheet = true
                                },
                                .default(Text(String(localized: "Catalog Select"))) {
                                   displayCatalogSelectInputSheet = true
                                },
                                .cancel()
                            ]
                        )
            }
            .sheet(isPresented: $displayImageInputSheet, onDismiss: { userPaletteViewModel.fetchUserPalettes() }, content: {
                CreatePaletteWithPhotosView()
                    .interactiveDismissDisabled()
            })
            .sheet(isPresented: $displayCatalogSelectInputSheet, onDismiss: { userPaletteViewModel.fetchUserPalettes() }, content: {
                PaletteCreationView()
                    .interactiveDismissDisabled()
            })
            .alert(String(localized: "Are you sure you want to clear your entire palette?"), isPresented: $displayClearUserPaletteConfirmationAlert) {
                Button(String(localized: "Yes"), role: .destructive) {
                    withAnimation(.easeOut) {
                        isEditing = false
                        isJiggling = false
                        userPaletteViewModel.deleteAllColoursFromUserPalette()
                    }
                }
                Button(String(localized: "Cancel"), role: .cancel) {
                    displayClearUserPaletteConfirmationAlert = false
                }
                .font(.defaultFontCaption)
            } // end of delete one colour alert
        }
    }
}


#Preview {
    UserPaletteView()
}

func delay(interval: TimeInterval, closure: @escaping () -> Void) {
    DispatchQueue.main.asyncAfter(deadline: .now() + interval, execute: closure)
}


@available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
extension View {

    @ViewBuilder
    func searchable(
        if condition: Bool,
        text: Binding<String>,
        placement: SearchFieldPlacement = .automatic,
        prompt: String
    ) -> some View {
        if condition {
            self.searchable(
                text: text,
                placement: placement,
                prompt: prompt
            )
        } else {
            self
        }
    }
}
